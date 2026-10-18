"""Vault: the bot's code, scripts, state and picture library live encrypted in vault.enc (AES via Fernet).
Only a GitHub run with the REPO_KEY secret can unlock them; the repo can be public and nobody can read or use
the files without the key. This bootstrap does only two harmless things - unlock and lock - and holds no secret.
    python vault/boot.py open     decrypt vault.enc -> bot/ series/ state/ library/
    python vault/boot.py seal     pack those dirs -> vault.enc"""
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


def seal():
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for d in DIRS:
            p = os.path.join(ROOT, d)
            if os.path.isdir(p):
                tar.add(p, arcname=d)
    with open(VAULT, "wb") as f:
        f.write(fernet().encrypt(buf.getvalue()))
    print(f"vault sealed ({os.path.getsize(VAULT) / 1e6:.1f} MB)")


def open_():
    if not os.path.exists(VAULT):
        print("no vault yet - first run")
        return
    data = fernet().decrypt(open(VAULT, "rb").read())
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        try:
            tar.extractall(ROOT, filter="data")
        except TypeError:
            tar.extractall(ROOT)
    print("vault opened")


if __name__ == "__main__":
    {"open": open_, "seal": seal}[sys.argv[1]]()
