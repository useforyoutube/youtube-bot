"""Daily cloud run. Works through state/queue.json (episode modules in series/, in order):
    pictures -> full video -> its Shorts -> upload (scheduled into prime-time slots) -> verify -> clean up
Stops cleanly (and the next run continues) when a free limit is reached:
    Cloudflare pictures (daily), YouTube quota (daily), GitHub minutes (monthly), or this job's time budget.
    python bot/run.py [--max-hours 4.5]"""
import datetime
import json
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import OUTPUT, ROOT, STATE  # noqa: E402
import uploader  # noqa: E402

START = time.time()
QUEUE = os.path.join(STATE, "queue.json")
MINUTES = os.path.join(STATE, "minutes.json")
MONTH_CAP = 1900                     # of GitHub's 2,000 free private-repo minutes a month
PY = sys.executable
BOT = os.path.dirname(os.path.abspath(__file__))


def log(msg):
    print(f"[bot {datetime.datetime.utcnow():%Y-%m-%d %H:%M} UTC] {msg}", flush=True)


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def month():
    return datetime.datetime.utcnow().strftime("%Y-%m")


def minutes_used():
    return load(MINUTES, {}).get(month(), 0)


def record_minutes():
    data = load(MINUTES, {})
    data[month()] = data.get(month(), 0) + int((time.time() - START) / 60) + 2     # +2: setup/teardown
    save(MINUTES, data)


class Stop(Exception):
    pass


def hours_left(max_hours):
    return max_hours - (time.time() - START) / 3600


def run(args, label):
    log(label)
    r = subprocess.run([PY, "-u", *args], cwd=BOT, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return r.returncode


def pictures(ep):
    code = run(["myth_images.py", ep], f"pictures for {ep}")
    if code == 3:
        raise Stop("Cloudflare daily picture limit - continuing after the 05:30 IST reset")
    if code != 0:
        raise RuntimeError(f"pictures failed for {ep}")


def render(ep, short=None):
    name = ep if short is None else f"{ep}_short{short + 1}"
    mp4 = os.path.join(OUTPUT, name, f"{name}.mp4")
    if os.path.exists(mp4 + ".done"):
        return mp4
    args = ["cine.py", ep] + ([] if short is None else ["--short", str(short)])
    for attempt in range(3):
        if run(args, f"render {name}") == 0 and os.path.exists(mp4):
            open(mp4 + ".done", "w").close()
            return mp4
        time.sleep(30)
    raise RuntimeError(f"render failed: {name}")


def meta(ep, short=None):
    out = os.path.join(OUTPUT, ep if short is None else f"{ep}_short{short + 1}")
    run(["cine.py", ep, "--meta-only"] + ([] if short is None else ["--short", str(short)]), f"metadata {ep}")
    return out, load(os.path.join(out, "meta.json" if short is None else "short_meta.json"), None)


def do_episode(ep, max_hours, n_shorts, after_title=None):
    import importlib
    m = importlib.import_module(ep)
    n_shorts = min(n_shorts, len(m.SHORTS))
    pub = uploader.published()
    if all(k in pub for k in [ep] + [f"{ep}_short{k + 1}" for k in range(n_shorts)]):
        return True
    pictures(ep)
    renders_needed = (ep not in pub) + sum(f"{ep}_short{k + 1}" not in pub for k in range(n_shorts))
    long_left = ep not in pub
    if hours_left(max_hours) < 1.8 * long_left + 0.35 * (renders_needed - long_left) + 0.2:
        raise Stop("not enough time left in this run for the renders - continuing next run")

    if ep not in pub:
        mp4 = render(ep)
        out, md = meta(ep)
        not_before = None
        if after_title:                                  # the previous part (uploaded elsewhere) must be on YouTube first
            prev = uploader.find_upload(after_title)
            if not prev:
                raise Stop(f"{ep} is ready, waiting for '{after_title}' to be on YouTube first")
            not_before = prev[1]
        vid = uploader.upload(ep, mp4, md, "long", os.path.join(out, "thumbnail.jpg"), not_before=not_before)
        uploader.verify(vid, md)
    for k in range(n_shorts):
        key = f"{ep}_short{k + 1}"
        if key in uploader.published():
            continue
        mp4 = render(ep, k)
        out, md = meta(ep, k)
        md["description"] = md["description"].replace("{FULL_EPISODE}", f"https://youtu.be/{uploader.published()[ep]}")
        vid = uploader.upload(key, mp4, md, "short")
        uploader.verify(vid, md)
    cleanup(ep, n_shorts)
    return True


def cleanup(ep, n_shorts):
    """video/audio files go as soon as they are on YouTube; pictures stay in the work cache until the series ends"""
    for name in [ep] + [f"{ep}_short{k + 1}" for k in range(n_shorts)]:
        d = os.path.join(OUTPUT, name)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.endswith((".mp4", ".wav")) and not f.endswith(".done"):
                os.remove(os.path.join(d, f))
        shutil.rmtree(os.path.join(d, "tts_cache"), ignore_errors=True)
        if name != ep:                                   # Short folders hold nothing worth keeping
            shutil.rmtree(d, ignore_errors=True)


def health():
    """once per run: logins work, limits left"""
    uploader.credentials()
    if sys.platform != "win32":
        from PIL import features
        if not features.check("raqm"):
            raise SystemExit("Hindi text shaping (raqm) missing - install libraqm0 / libfribidi0")
    for k in ("CF_ACCOUNT_ID", "CF_TOKEN"):
        if uploader.os.environ.get("GITHUB_ACTIONS") and not os.environ.get(k):
            raise SystemExit(f"missing secret {k}")
    log(f"health ok | YouTube quota used today {uploader.used()} | GitHub minutes this month {minutes_used()}")


def selftest():
    """render the tiny self-test video (never uploaded) - proves text, voice, music, render and login work"""
    health()
    pictures("selftest")
    mp4 = render("selftest")
    out = os.path.join(OUTPUT, "selftest")
    assert os.path.getsize(mp4) > 200_000, "self-test video too small"
    assert os.path.exists(os.path.join(out, "thumbnail.jpg")), "no thumbnail"
    log(f"SELF-TEST PASSED: {mp4}")
    return mp4


def main():
    if "--selftest" in sys.argv:
        try:
            selftest()
        finally:
            record_minutes()
        return
    max_hours = float(sys.argv[sys.argv.index("--max-hours") + 1]) if "--max-hours" in sys.argv else 4.5
    q = load(QUEUE, {"episodes": [], "shorts_per_episode": 2})
    try:
        if minutes_used() >= MONTH_CAP:
            raise Stop(f"GitHub minutes for {month()} nearly used ({minutes_used()}) - waiting for next month")
        health()
        for item in q["episodes"]:
            item = item if isinstance(item, dict) else {"ep": item}
            ep = item["ep"]
            if ep in q.get("done", []):
                continue
            do_episode(ep, max_hours, item.get("shorts", q.get("shorts_per_episode", 2)), item.get("after_title"))
            q.setdefault("done", []).append(ep)
            save(QUEUE, q)
            log(f"{ep} complete")
        log("queue empty - nothing more to do")
    except (Stop, uploader.QuotaWait) as e:
        log(f"stopping for now: {e}")
    finally:
        record_minutes()


if __name__ == "__main__":
    main()
