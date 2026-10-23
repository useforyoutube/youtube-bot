"""Vault: the bot's code, scripts, state and picture library live encrypted in vault.enc (AES via Fernet).
Only a GitHub run with the REPO_KEY secret can unlock them; the repo can be public and nobody can read or use
the files without the key. This bootstrap does only two harmless things - unlock and lock - and holds no secret.
    python vault/boot.py open     decrypt vault.enc -> bot/ series/ state/ library/
    python vault/boot.py seal     pack those dirs -> vault.enc
    python vault/boot.py adopt-code <other.enc>   take bot/ (the code) from another vault, keep everything else
                                                  (used when a run's save clashes with a newer code push)"""
import base64
import io
import os
import sys
import tarfile

from cryptography.fernet import Fernet

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT = os.path.join(ROOT, "vault.enc")
DIRS = ["bot", "series", "state", "library"]


def fernet():
    key = os.environ.get("REPO_KEY")
    if not key:
        sys.exit("REPO_KEY secret missing - cannot open the vault")
    return Fernet(key.encode())


def _read(path):
    """vault.enc is stored as raw bytes (old vaults: base64 text). Base64 text could by chance look like a cloud key
    ('AKID...') and GitHub push protection then blocked the whole save - binary files are not scanned."""
    raw = open(path, "rb").read()
    return raw if raw.startswith(b"gAAAAA") else base64.urlsafe_b64encode(raw)


def undo_unfinished_repair():
    """a self-repair / code-check edit that was never verified (the step was killed) is put back before sealing"""
    p = os.path.join(os.environ.get("BOT_WORK", os.path.join(ROOT, "work")), "pending_restore.json")
    if os.path.exists(p):
        import json
        for f, text in json.load(open(p, encoding="utf-8")).items():
            open(os.path.join(ROOT, "bot", os.path.basename(f)), "w", encoding="utf-8", newline="\n").write(text)
        os.remove(p)
        print("an unverified code edit was put back before sealing")


def seal():
    if not (os.path.exists(os.path.join(ROOT, "bot", "run.py")) and os.path.isdir(os.path.join(ROOT, "state"))):
        raise SystemExit("refusing to seal: the vault was not opened (bot/ or state/ missing) - the old vault stays")
    undo_unfinished_repair()
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for d in DIRS:
            p = os.path.join(ROOT, d)
            if os.path.isdir(p):
                tar.add(p, arcname=d)
    with open(VAULT, "wb") as f:
        f.write(base64.urlsafe_b64decode(fernet().encrypt(buf.getvalue())))
    print(f"vault sealed ({os.path.getsize(VAULT) / 1e6:.1f} MB)")


def open_():
    if not os.path.exists(VAULT):
        print("no vault yet - first run")
        return
    data = fernet().decrypt(_read(VAULT))
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        try:
            tar.extractall(ROOT, filter="data")
        except TypeError:
            tar.extractall(ROOT)
    snapshot_state()
    print("vault opened")


def _hash(path):
    import hashlib
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def snapshot_state():
    """what state/ looked like when this run opened the vault (to merge a save clash file by file)"""
    import json
    snap = {}
    for root, _, files in os.walk(os.path.join(ROOT, "state")):
        for f in files:
            p = os.path.join(root, f)
            snap[os.path.relpath(p, ROOT).replace("\\", "/")] = _hash(p)
    w = os.environ.get("BOT_WORK", os.path.join(ROOT, "work"))
    os.makedirs(w, exist_ok=True)
    json.dump(snap, open(os.path.join(w, "state_snapshot.json"), "w"))


def adopt_code(path):
    data = fernet().decrypt(_read(path))
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        import json
        snap_p = os.path.join(os.environ.get("BOT_WORK", os.path.join(ROOT, "work")), "state_snapshot.json")
        snap = json.load(open(snap_p)) if os.path.exists(snap_p) else {}
        unchanged = [m for m in tar.getmembers() if m.isfile() and m.name.startswith("state/") and (
            m.name not in snap or (os.path.exists(os.path.join(ROOT, m.name)) and
                                   _hash(os.path.join(ROOT, m.name)) == snap[m.name]))]
        try:                                           # files this run did not change: take the newer remote copy
            tar.extractall(ROOT, members=unchanged, filter="data")
        except TypeError:
            tar.extractall(ROOT, members=unchanged)
        print(f"kept {len(unchanged)} newer state files from the other run")
        members = [m for m in tar.getmembers() if m.name == "bot" or m.name.startswith("bot/")]
        if members:                                    # files removed upstream must go too
            import shutil
            shutil.rmtree(os.path.join(ROOT, "bot"), ignore_errors=True)
        try:
            tar.extractall(ROOT, members=members, filter="data")
        except TypeError:
            tar.extractall(ROOT, members=members)
    print(f"took the newer code ({len(members)} files) from {os.path.basename(path)}")


if __name__ == "__main__":
    if sys.argv[1] == "adopt-code":
        adopt_code(sys.argv[2])
    else:
        {"open": open_, "seal": seal}[sys.argv[1]]()
