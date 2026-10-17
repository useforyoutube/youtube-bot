"""Cinematic story videos from AI paintings, told like a film.
  python cine.py <module>            full episode, 1920x1080, with chapters, thumbnail and meta.json
  python cine.py <module> --short K  vertical Short (1080x1920) from module.SHORTS[K]
  add --audio-only to rebuild just the soundtrack of an existing render.
Every video carries the disclaimer, a subscribe + share request and the copyright line.
Characters talk: their mouth moves with their voice (face found automatically, or set in module.TALK)."""
import asyncio
import hashlib
import importlib
import json
import math
import os
import re
import subprocess
import sys
import time
import wave

import edge_tts
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import toolkit as bt
from paths import MODELS, MUSIC, OUTPUT, STATE
import thumbs
from quiet import wait_if_quiet

FPS, SR = 24, bt.SR
GOLD, WHITE, RED = (255, 214, 120), (250, 246, 238), (190, 20, 30)
MUSIC_DIRS = [MUSIC]
MUSIC_URL = "https://incompetech.com/music/royalty-free/mp3-royaltyfree/"
DISSOLVE = 0.7
# colour grades (r, g, b) - one is picked per episode / Short; the first is the original warm look
GRADES = [(1.04, 0.98, 0.90), (0.97, 1.00, 1.05), (1.07, 1.00, 0.84), (1.03, 0.95, 1.00), (1.00, 1.00, 0.97),
          (1.05, 0.99, 0.93)]
DARK = re.compile(r"kali|demon|asur|koka|vikoka|night|dark|ravana|hiranya|durukti|storm|black|burn|army_tired")
EMBERS = re.compile(r"battle|war|fight|fire|burn|attack|charge|strike|yajna|ashes|ravana|narasimha|koka_vs")
DUST = re.compile(r"vishnu|shiva|brahma|divine|glow|boon|temple|blessing|hamsa|dhanvantari|krishna|rama|buddha|"
                  r"kumaras|narada|meditat|tapasya|flowers")
MUSIC_LEVEL = 0.17                  # music RMS before ducking; only dipped 30% under the voice
SUBSCRIBE = "सब्सक्राइब करें  •  शेयर करें"
COPY = "© 2026 Sujay Ganguly Creations"
rng = np.random.default_rng(7)

WIDE = dict(W=1920, H=1080, title=(420, 560), series=58, sub=(975, 52, 44), who=905, cta=(430, 560, 660),
            disc=(1012, 30, 70), pill=860)
TALL = dict(W=1080, H=1920, title=(330, 470), series=150, sub=(1500, 58, 24), who=1395, cta=(800, 930, 1040),
            disc=(1700, 34, 30), pill=1270)


# ---------------------------------------------------------------- audio

def lowpass(x, k):
    return np.convolve(x, np.ones(k, np.float32) / k, mode="same").astype(np.float32)


def boom():
    t = np.arange(int(1.8 * SR)) / SR
    f = 28 + 50 * np.exp(-t * 5)
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2) * 0.5).astype(np.float32)


def reverb(a, taps):
    r = a.copy()
    for d, g in taps:
        k = int(d * SR)
        r[k:] += a[:-k] * g
    return r


def process(a, effect):
    if effect == "narrator":
        return reverb(a + lowpass(a, 12) * 0.35, ((0.05, 0.16), (0.11, 0.1), (0.19, 0.06)))
    if effect == "demon":
        a = np.tanh((a + lowpass(a, 20) * 0.8) * 2.2) * 0.6
        return reverb(a, ((0.09, 0.45), (0.21, 0.3), (0.38, 0.2), (0.6, 0.12)))
    if effect == "divine":                            # vast temple-like space
        return reverb(a, ((0.07, 0.35), (0.16, 0.28), (0.29, 0.2), (0.45, 0.14), (0.7, 0.08)))
    if effect == "soft":
        return reverb(a, ((0.06, 0.12), (0.14, 0.07)))
    return a


def speak(text, voice, folder):
    """Phrase by phrase so '...' becomes a real dramatic pause; returns audio + phrase timings."""
    os.makedirs(folder, exist_ok=True)
    out, phrases, pos = [], [], 0
    for p in [p.strip() for p in re.split(r"(\.\.\.)", text)]:
        if p == "...":
            out.append(np.zeros(int(0.55 * SR), np.float32))
            pos += len(out[-1])
            continue
        if not p:
            continue
        path = os.path.join(folder, hashlib.md5(f"{p}|{voice}".encode()).hexdigest()[:14] + ".mp3")
        a = None
        for attempt in range(4):
            if not os.path.exists(path):
                try:                                   # write to .part first: a dropped connection never leaves
                    asyncio.run(edge_tts.Communicate(p, voice[0], rate=voice[1], pitch=voice[2]).save(path + ".part"))
                    os.replace(path + ".part", path)    # a half-written clip in the cache
                except Exception:
                    if attempt == 3:
                        raise
                    time.sleep(10 * (attempt + 1))
                    continue
            try:
                a = bt.load_audio(path)
                break
            except Exception:                          # broken clip from an older run: make it again
                os.replace(path, path + ".bad")
                if attempt == 3:
                    raise
        nz = np.nonzero(np.abs(a) > 0.01)[0]
        a = a[max(0, nz[0] - 200): nz[-1] + 1200] if len(nz) else a
        phrases.append((pos / SR, len(a) / SR, p))
        out.append(a)
        pos += len(a)
    return process(np.concatenate(out), voice[3]), phrases


def track(name, offset, n):
    for d in MUSIC_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            a = bt.load_audio(p)[int(offset * SR):]
            return np.tile(a, n // max(1, len(a)) + 1)[:n]
    import urllib.parse                             # Kevin MacLeod (CC BY): download once, cached between runs
    import urllib.request
    os.makedirs(MUSIC, exist_ok=True)
    p = os.path.join(MUSIC, name)
    urllib.request.urlretrieve(MUSIC_URL + urllib.parse.quote(name), p + ".part")
    os.replace(p + ".part", p)
    return track(name, offset, n)


# ---------------------------------------------------------------- talking faces

def find_mouth(path):
    """Mouth centre / lip line / size from the YuNet face detector (models/yunet.onnx), or None."""
    import cv2
    img = cv2.imread(path)
    h, w = img.shape[:2]
    det = cv2.FaceDetectorYN.create(os.path.join(MODELS, "yunet.onnx"), "", (w, h), 0.6)
    _, faces = det.detect(img)
    if faces is None or not len(faces):
        return None
    f = max(faces, key=lambda f: f[2] * f[3])
    fh = f[3]
    cx, cy = (f[10] + f[12]) / 2, (f[11] + f[13]) / 2 + 0.035 * fh
    hw = max(10.0, abs(f[12] - f[10]) / 2)
    return float(cx), float(cy), float(hw), float(0.33 * fh), float(max(4.0, 0.055 * fh))


def talk(arr, cx, cy, hw, depth, op):
    """Open a painted mouth: shift the jaw below the lip line down and show a dark mouth interior."""
    if op < 0.6:
        return arr
    x0, x1 = int(cx - hw * 1.3), int(cx + hw * 1.3)
    y0, y1 = int(cy), int(min(arr.shape[0], cy + depth))
    reg = arr[y0:y1, x0:x1]
    X = np.linspace(-1.3, 1.3, x1 - x0, dtype=np.float32)
    fx = np.clip(1 - X ** 2, 0, 1)
    Y = np.arange(y1 - y0, dtype=np.float32)[:, None]
    S = op * fx[None, :]
    src = Y - S * (1 - Y / depth)
    gap = src < 0
    idx = np.clip(np.round(src), 0, y1 - y0 - 1).astype(np.int32)
    out = np.take_along_axis(reg, np.repeat(idx[:, :, None], 3, axis=2), axis=0)
    din = np.clip(-src / np.maximum(S, 1), 0, 1)[:, :, None]
    inner = np.array([70, 14, 22], np.float32) * (1 - din) + np.array([12, 4, 6], np.float32) * din
    shade = np.clip(-src / 2.5, 0, 1)[:, :, None]
    out = np.where(gap[:, :, None], out * (1 - shade) + inner * shade, out)
    arr = arr.copy()
    arr[y0:y1, x0:x1] = out
    return arr


# ---------------------------------------------------------------- build

def fmt(s):
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


CHANNEL_NAME = "Sujay Ganguly Creations"
CHANNEL_HANDLE = "@sujaygangulycreations"
LOCATION_LINE = "📍 India | भारत"
WEAK_TAGS = ["kalki 2898 ad", "yug parivartan", "kaliyuga", "kalki avtar", "kalyug", "kali purush"]


def write_meta(m, short, out, chap_times):
    """meta.json / short_meta.json for youtube_upload.py ({FULL_EPISODE} is filled in at upload time)."""
    seo = m.SEO if short is None else m.SHORTS[short]["seo"]
    desc = seo["description"].replace("{CHAPTERS}", "\n".join(f"{fmt(ct)} {title}" for ct, title in chap_times))
    desc = desc.replace("{MUSIC_CREDIT}", m.MUSIC_CREDIT).replace("{DISCLAIMER}", m.DISCLAIMER)
    desc = re.sub(r"\s*https?://creativecommons\.org/\S*", "", desc)     # external links block Studio edits
    if CHANNEL_HANDLE not in desc:
        desc = desc.replace("\n© ", f"\n{CHANNEL_HANDLE}\n\n© ", 1)
    if LOCATION_LINE not in desc:                     # location: YouTube's API can't set it, so tags + text
        desc = (desc.replace("\n© ", f"\n{LOCATION_LINE}\n\n© ", 1) if "\n© " in desc
                else desc + "\n" + LOCATION_LINE)
    tags = seo["tags"] + ([CHANNEL_NAME] if CHANNEL_NAME not in seo["tags"] else [])
    tags += [t for t in ("India", "भारत") if t not in tags]
    tag_len = lambda ts: sum(len(t) + (2 if " " in t else 0) + 1 for t in ts)
    for weak in WEAK_TAGS:                                          # stay under YouTube's 500-char tag limit
        if tag_len(tags) <= 495:
            break
        if weak in tags:
            tags.remove(weak)
    meta = dict(title=seo["title"], description=desc, tags=tags, categoryId=seo.get("categoryId", "24"),
                defaultLanguage="hi", defaultAudioLanguage="hi", privacyStatus="public", madeForKids=False,
                containsSyntheticMedia=True, location=dict(latitude=20.593684, longitude=78.96288),
                locationDescription="India")
    pl_path = os.path.join(STATE, "playlists.json")
    if getattr(m, "PLAYLIST", None) and os.path.exists(pl_path):
        meta["playlistId"] = json.load(open(pl_path))[m.PLAYLIST]
    json.dump(meta, open(os.path.join(out, "meta.json" if short is None else "short_meta.json"), "w",
                         encoding="utf-8"), ensure_ascii=False, indent=2)


def main(name):
    m = importlib.import_module(name)
    short = int(sys.argv[sys.argv.index("--short") + 1]) if "--short" in sys.argv else None
    L = TALL if short is not None else WIDE
    W, H = L["W"], L["H"]
    base = os.path.join(OUTPUT, name)
    out = base if short is None else f"{base}_short{short + 1}"
    os.makedirs(out, exist_ok=True)
    bt.TEXT_DIR = os.path.join(base, "text_cache")
    imgdir = os.path.join(base, "img")
    imgs = {k: Image.open(os.path.join(imgdir, f"{k}.jpg")).convert("RGB") for k, _ in m.IMAGES}
    wait_if_quiet("cinematic video")

    # lines + chapter markers
    lines, chapters = [], []
    for row in m.LINES:
        if row[0] == "#":
            chapters.append((len(lines), row[1]))
        else:
            lines.append(row)
    if short is not None:
        sp = m.SHORTS[short]

        def at(v, last=False):                         # a line index, or the image key shown on that line
            if isinstance(v, int):
                return v
            hits = [i for i, row in enumerate(lines) if v in row[0]]
            return hits[-1] if last else hits[0]
        lines = lines[at(sp["from"]): at(sp["to"], True) + 1]
        chapters = []
        hook, hook2 = sp["hook"], sp.get("hook2", m.SERIES)
    else:
        hook, hook2 = m.HOOK, m.HOOK2

    segs, t = [], (1.2 if short is not None else 6.0)       # long: room for the disclaimer + title
    for keys, who, line, fx in lines:
        a, phrases = speak(line, m.VOICES[who], os.path.join(base, "tts_cache"))
        lead, tail = (0.5, 0.9) if fx else (0.35, 0.6)
        hop = SR // FPS
        nfr = len(a) // hop
        env = np.sqrt((a[:nfr * hop].reshape(nfr, hop) ** 2).mean(axis=1))
        env = np.clip(env / (np.percentile(env[env > 0.01], 85) if (env > 0.01).any() else 1), 0, 1)
        env = np.convolve(env, [0.25, 0.5, 0.25], mode="same")
        segs.append(dict(keys=keys, who=who, start=t, dur=lead + len(a) / SR + tail, lead=lead, audio=a, fx=fx,
                         env=env, subs=[(t + lead + p0, t + lead + p0 + d, p) for p0, d, p in phrases]))
        t += segs[-1]["dur"]
    end_card = 6.0 if short is None else 4.0
    total = t + end_card
    chap_times = [(0.0 if i == 0 else segs[li]["start"], title) for i, (li, title) in enumerate(chapters)]
    if "--meta-only" in sys.argv:
        write_meta(m, short, out, chap_times)
        if short is None and thumbs.design(name):        # newest thumbnail design right before upload
            thumbs.make(name)
        print("meta written:", out)
        return

    cta_main = m.NEXT if short is None else "पूरा एपिसोड चैनल पर देखें"
    texts = [(hook, 118 if short is not None else 110), (hook2, 80), (m.SERIES, 38), (cta_main, 72),
             (SUBSCRIBE, 60), (m.DISCLAIMER_SHORT, L["disc"][1]), ("सब्सक्राइब करें", 40)]
    texts += [(bt.wrap(p, L["sub"][2]), L["sub"][1]) for s in segs for _, _, p in s["subs"]]
    texts += [(n_, 40) for n_, _ in m.SPEAKERS.values()]
    if short is None:
        texts += [(bt.wrap(m.DISCLAIMER, 34), 50)] + [(title, 64) for _, title in chap_times]
        texts += [(x[0], x[1]) for x in getattr(m, "THUMB", {}).get("text", [])]
    bt.prepare_text(texts)

    def fit(text, size, stroke):
        """shrink a big title so it never runs off the frame (Shorts are only 1080 px wide)"""
        return min(1.0, 0.92 * W / bt.mask(text, size, stroke).width)

    # ---- audio
    n = int(total * SR)
    voice, vm, fxbus = np.zeros(n, np.float32), np.zeros(n, np.float32), np.zeros(n, np.float32)

    def add(buf, sig, at, g=1.0):
        s = int(at * SR)
        sig = sig[: max(0, n - s)]
        buf[s:s + len(sig)] += sig * g

    for s in segs:
        add(voice, s["audio"], s["start"] + s["lead"], 1.2)
        a0 = int((s["start"] + s["lead"]) * SR)
        vm[a0:a0 + len(s["audio"])] = 1
        if s["fx"] == "thunder":
            add(fxbus, bt.sfx("thunder") * 0.7, s["start"])
            add(fxbus, boom(), s["start"], 0.8)
    music = np.zeros(n, np.float32)
    plan = []
    for when, trk, off in (m.MUSIC_PLAN if short is None else m.SHORTS[short].get("music", m.MUSIC_PLAN[:1])):
        if isinstance(when, str):
            hit = [s["start"] for s in segs if when in s["keys"]]
            if not hit:
                continue
            when = hit[0] - 0.4
        plan.append((max(0.0, when), trk, off))
    xf = int(1.5 * SR)
    for i, (when, trk, off) in enumerate(plan):
        s0 = int(when * SR)
        s1 = min(n, int(plan[i + 1][0] * SR) + xf) if i + 1 < len(plan) else n
        if s1 <= s0:
            continue
        seg = track(trk, off, s1 - s0)
        env = np.ones(len(seg), np.float32)
        if i:
            env[:xf] = np.linspace(0, 1, xf)
        if i + 1 < len(plan):
            env[-xf:] = np.linspace(1, 0, xf)
        music[s0:s1] += seg * env
    fi, fo = int(1.5 * SR), int(3.0 * SR)
    music[:fi] *= np.linspace(0.2, 1, fi)
    music[-fo:] *= np.linspace(1, 0, fo)
    k = int(0.3 * SR)
    c = np.cumsum(np.concatenate([[0], vm]))
    duck = np.concatenate([(c[k:] - c[:-k]) / k, np.zeros(k)])[:n].astype(np.float32)
    mix = voice + fxbus + music / (np.sqrt(np.mean(music ** 2)) or 1) * MUSIC_LEVEL * (1 - 0.3 * duck)
    mix = np.tanh(mix * 1.3) * 0.9
    wav = os.path.join(out, "audio.wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())
    mp4 = os.path.join(out, f"{name}{'' if short is None else f'_short{short + 1}'}.mp4")
    if "--audio-only" in sys.argv and os.path.exists(mp4):
        tmp = mp4[:-4] + "_tmp.mp4"
        subprocess.run([bt.FFMPEG, "-y", "-v", "error", "-i", mp4, "-i", wav, "-map", "0:v", "-map", "1:a",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", tmp],
                       check=True)
        os.replace(tmp, mp4)
        print(f"Audio replaced: {mp4}")
        return

    # ---- talking faces
    talk_at = {}
    manual = getattr(m, "TALK", {})
    mouth_cache = os.path.join(base, "mouths.json")
    cache = json.load(open(mouth_cache)) if os.path.exists(mouth_cache) else {}
    for s in segs:
        if s["who"] == "N":
            continue
        for key in s["keys"]:
            if key in manual:
                talk_at[key] = manual[key][1:]
            else:
                if key not in cache:
                    cache[key] = find_mouth(os.path.join(imgdir, f"{key}.jpg"))
                if cache[key]:
                    talk_at[key] = tuple(cache[key])
    json.dump(cache, open(mouth_cache, "w"))
    srcs = {k: np.asarray(imgs[k]).astype(np.float32) for k in talk_at}

    # ---- picture
    yy = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
    xx = np.linspace(-1, 1, W, dtype=np.float32)[None, :, None]
    look = (1 - 0.45 * np.clip(1 - yy / 0.2, 0, 1) - 0.55 * np.clip((yy - 0.66) / 0.34, 0, 1)) * \
           (1 - 0.3 * xx ** 2) * np.array([1.04, 0.98, 0.9], np.float32)
    grain = [rng.normal(0, 2.5, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1) for _ in range(6)]
    shots = []
    for si, s in enumerate(segs):
        for j, key in enumerate(s["keys"]):
            d = s["dur"] / len(s["keys"])
            shots.append((s["start"] + j * d, d, key, len(shots), s["fx"] if j == 0 else "", si))
    shots[0] = (0.0, shots[0][1] + segs[0]["start"], *shots[0][2:])
    shots.append((t, end_card, segs[-1]["keys"][-1], len(shots), "end", -1))
    subs = [(a, b, bt.wrap(p, L["sub"][2]), s["who"]) for s in segs for a, b, p in s["subs"]]
    pills = [] if short is not None else [total * 0.3, total * 0.65]

    def cover(img, zoom, panx, pany):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
        sc = max(W / img.width, H / img.height) * zoom
        w, h = int(img.width * sc), int(img.height * sc)
        x0 = int((w - W) / 2 * (1 + panx))
        y0 = int((h - H) / 2 * (1 + pany))
        return img.resize((w, h), Image.BILINEAR).crop((x0, y0, x0 + W, y0 + H))

    # ---- variety: every episode (and each Short) gets its own camera moves, colour grade and atmosphere,
    # so the series never looks like one template repeated
    vr = np.random.default_rng(int(hashlib.md5(f"{name}|{short}".encode()).hexdigest()[:8], 16))
    look = look * np.array(GRADES[vr.integers(len(GRADES))], np.float32) / np.array([1.04, 0.98, 0.9], np.float32)
    MOVES = [(-0.4, 0.4, 0, 0), (0.4, -0.4, 0, 0), (0, 0, 0.35, -0.35), (0, 0, -0.3, 0.3),
             (0.3, -0.3, 0.25, -0.25), (-0.3, 0.3, 0.25, -0.25), (0, 0, 0, 0), (0.15, -0.15, -0.15, 0.15)]
    motion = []
    for _ in shots:
        x0, x1, y0, y1 = MOVES[vr.integers(len(MOVES))]
        push = vr.random() < 0.7
        z0, z1 = (1.04, 1.04 + vr.uniform(0.06, 0.13)) if push else (1.17, 1.07)
        motion.append((x0, x1, y0, y1, z0, z1))
    chap_starts = [ct for ct, _ in chap_times[1:]]
    dips = {j for j, sh in enumerate(shots) if any(abs(sh[0] - ct) < 0.6 for ct in chap_starts)}
    tint = {}
    for k in imgs:
        tint[k] = np.array([0.9, 0.94, 1.1], np.float32) if DARK.search(k) else np.ones(3, np.float32)
    parts = vr.random((90, 6)).astype(np.float32)                 # x, y, speed, size, phase, drift

    def atmosphere(key, tt):
        kind = "embers" if EMBERS.search(key) else "dust" if DUST.search(key) else None
        if kind is None:
            return None
        h4, w4 = H // 4, W // 4
        layer = np.zeros((h4, w4), np.float32)
        sp = 0.06 if kind == "embers" else 0.015
        x = (parts[:, 0] + np.sin(tt * 0.7 + parts[:, 4] * 6.3) * 0.02 * parts[:, 5]) % 1.0
        y = (parts[:, 1] - tt * sp * (0.5 + parts[:, 2])) % 1.0
        xi, yi = (x * (w4 - 2)).astype(int), (y * (h4 - 2)).astype(int)
        b = (0.6 + 0.4 * np.sin(tt * 3 + parts[:, 4] * 9)) * (1.0 if kind == "embers" else 0.7)
        layer[yi, xi] = b
        layer[yi + 1, xi] = b * (parts[:, 3] > 0.5)
        lay = Image.fromarray((np.clip(layer, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
        lay = np.asarray(lay.resize((W, H), Image.BILINEAR)).astype(np.float32)[..., None] / 255.0
        col = np.array([255, 140, 40] if kind == "embers" else [255, 220, 150], np.float32)
        return lay * col * 0.9

    def paint(shot, lt):
        st, d, key, idx, fx, si = shot
        q = min(1.3, lt / (d + DISSOLVE))
        x0, x1, y0, y1, z0, z1 = motion[idx]
        src = imgs[key]
        if key in talk_at and si >= 0 and segs[si]["who"] != "N":
            sg = segs[si]
            k = int((st + lt - sg["start"] - sg["lead"]) * FPS)
            if 0 <= k < len(sg["env"]):
                cx, cy, hw, depth, mx = talk_at[key]
                src = talk(srcs[key], cx, cy, hw, depth, mx * sg["env"][k])
        arr = np.asarray(cover(src, z0 + (z1 - z0) * q, x0 + (x1 - x0) * q, y0 + (y1 - y0) * q)).astype(np.float32)
        return arr * tint[key]

    def faded(col, k):
        return tuple(int(c * k) for c in col)

    proc = subprocess.Popen([bt.FFMPEG, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                             "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest",
                             "-movflags", "+faststart", mp4], stdin=subprocess.PIPE)
    for f in range(int(total * FPS)):
        if f % (FPS * 10) == 0:
            wait_if_quiet(f"render of {name}")
            if f % (FPS * 60) == 0:
                print(f"  {fmt(f / FPS)} / {fmt(total)}", flush=True)
        tt = f / FPS
        i = max(j for j, sh in enumerate(shots) if sh[0] <= tt or j == 0)
        sh = shots[i]
        lt = tt - sh[0]
        arr = paint(sh, lt)
        if i in dips:                                   # new chapter: dip through black
            p = shots[i - 1]
            if lt < 0.35:
                arr = paint(p, p[1] + lt) * (1 - lt / 0.35)
            elif lt < 0.9:
                arr = arr * bt.ease((lt - 0.35) / 0.55)
        elif i and lt < DISSOLVE and sh[4] != "thunder":
            p = shots[i - 1]
            a = bt.ease(lt / DISSOLVE)
            arr = arr * a + paint(p, p[1] + lt) * (1 - a)
        if sh[4] == "thunder" and lt < 0.45:
            arr = arr + (255 - arr) * (1 - lt / 0.45) ** 2 * 0.8
        atm = atmosphere(sh[2], tt)
        if atm is not None:
            arr = arr + atm
        arr = arr * look + grain[f % 6]
        if sh[4] == "end":
            arr *= 0.45
        if short is None and tt < 6.0:                  # opening: disclaimer card, then the title over the picture
            arr *= 0.25 if tt < 3.2 else min(1.0, 0.25 + (tt - 3.2) / 0.8)
        img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        d = ImageDraw.Draw(img)
        if short is None and tt < 3.2:
            k = min(1.0, tt / 0.5, (3.2 - tt) / 0.4)
            bt.put_text(img, bt.wrap(m.DISCLAIMER, 34), 50, W / 2, H / 2, faded(WHITE, k))
        elif tt < (3.6 if short is not None else 9.0):
            t0 = 0.0 if short is not None else 3.4
            k = min(1.0, (tt - t0) / 0.8, ((3.6 if short is not None else 9.0) - tt) / 0.6)
            hs = 118 if short is not None else 110
            bt.put_text(img, hook, hs, W / 2, L["title"][0], faded(GOLD, k), stroke=8,
                        stroke_fill=(0, 0, 0), scale=fit(hook, hs, 8))
            bt.put_text(img, hook2, 80, W / 2, L["title"][1], faded(WHITE, k), stroke=6, stroke_fill=(0, 0, 0),
                        scale=fit(hook2, 80, 6))
            if short is not None and tt < 3.6:          # Shorts: the disclaimer as a small line
                bt.put_text(img, m.DISCLAIMER_SHORT, L["disc"][1], W / 2, L["disc"][0], faded((215, 215, 215), k),
                            stroke=3, stroke_fill=(0, 0, 0))
        else:
            bt.put_text(img, m.SERIES, 38, W / 2, L["series"], (225, 200, 160), stroke=4, stroke_fill=(0, 0, 0))
        for ct, title in chap_times[1:]:               # chapter title cards
            if ct <= tt < ct + 3.0:
                k = min(1.0, (tt - ct) / 0.5, (ct + 3.0 - tt) / 0.5)
                bt.put_text(img, title, 64, W / 2, L["title"][0] - 200, faded(GOLD, k), stroke=6,
                            stroke_fill=(0, 0, 0))
        for a0, a1, text, who in subs:
            if a0 - 0.1 <= tt < a1 + 0.35:
                k = min(1.0, (tt - a0 + 0.1) / 0.25, (a1 + 0.35 - tt) / 0.25)
                bt.put_text(img, text, L["sub"][1], W / 2, L["sub"][0], faded(WHITE, k), stroke=6,
                            stroke_fill=(0, 0, 0))
                if who in m.SPEAKERS:
                    nm, nc = m.SPEAKERS[who]
                    bt.put_text(img, nm, 40, W / 2, L["who"], faded(nc, k), stroke=5, stroke_fill=(0, 0, 0))
                break
        for p0 in pills:                                # mid-video subscribe reminder
            if p0 <= tt < p0 + 4.0:
                k = min(1.0, (tt - p0) / 0.4, (p0 + 4.0 - tt) / 0.4)
                pm = bt.mask("सब्सक्राइब करें", 40)
                x0 = W - pm.width - 120
                d.rounded_rectangle([x0, 40, x0 + pm.width + 70, 40 + pm.height + 30], 30, fill=faded(RED, k))
                bt.put_text(img, "सब्सक्राइब करें", 40, x0 + 35 + pm.width / 2, 55 + pm.height / 2, faded(WHITE, k))
        if sh[4] == "end":
            pop = bt.ease_back(lt / 0.5)
            bt.put_text(img, cta_main, 72, W / 2, L["cta"][0], GOLD, stroke=8, stroke_fill=(0, 0, 0),
                        scale=pop * fit(cta_main, 72, 8))
            sm = bt.mask(SUBSCRIBE, 60)
            y = L["cta"][1]
            d.rounded_rectangle([W / 2 - sm.width / 2 - 40, y - sm.height / 2 - 22, W / 2 + sm.width / 2 + 40,
                                 y + sm.height / 2 + 22], 34, fill=RED)
            bt.put_text(img, SUBSCRIBE, 60, W / 2, y, WHITE, scale=1 + 0.04 * math.sin(lt * 6))
        d.text((W - 24, H - 22) if short is None else (W / 2, H - 90), COPY, font=bt.efont(26),
               fill=(230, 230, 230), anchor="rd" if short is None else "mm", stroke_width=3, stroke_fill=(20, 15, 15))
        fade = min(1.0, tt / 0.8, (total - tt) / 1.0)
        frame = np.asarray(img).astype(np.float32) * fade if fade < 1 else np.asarray(img)
        proc.stdin.write(np.asarray(frame, np.uint8).tobytes())
    proc.stdin.close()
    proc.wait()

    # ---- thumbnail + meta for upload
    write_meta(m, short, out, chap_times)
    if short is None and thumbs.design(name):
        thumbs.make(name)
        bt.TEXT_DIR = os.path.join(base, "text_cache")
        print("Chapters:\n" + "\n".join(f"{fmt(ct)} {title}" for ct, title in chap_times))
    elif short is None:
        th = m.THUMB
        im = cover(imgs[th["image"]], th.get("zoom", 1.0), 0, th.get("pany", 0))
        im = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.25)).enhance(1.12)
        arr = np.asarray(im).astype(np.float32) * (1 - 0.5 * np.clip(1 - yy / 0.45, 0, 1))
        im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        for text, size, col, y in th["text"]:
            bt.put_text(im, text, size, W / 2, y, col, stroke=12, stroke_fill=(0, 0, 0))
        ImageDraw.Draw(im).text((W - 24, H - 22), COPY, font=bt.efont(30), fill=WHITE, anchor="rd", stroke_width=3,
                                stroke_fill=(20, 15, 15))
        im.resize((1280, 720), Image.LANCZOS).save(os.path.join(out, "thumbnail.jpg"), quality=92)
        print("Chapters:\n" + "\n".join(f"{fmt(ct)} {title}" for ct, title in chap_times))
    print(f"Done: {mp4} ({fmt(total)})")


if __name__ == "__main__":
    main(sys.argv[1])
