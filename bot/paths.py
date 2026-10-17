"""Where everything lives. ROOT = the repository; WORK = scratch space for pictures/renders (not committed;
on GitHub it is restored from the Actions cache between runs)."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "state")
SERIES = os.path.join(ROOT, "series")
LIBRARY = os.path.join(ROOT, "library")          # small, capped character library (committed)
MODELS = os.path.join(ROOT, "models")
WORK = os.environ.get("BOT_WORK") or os.path.join(ROOT, "work")
OUTPUT = os.path.join(WORK, "output")
MUSIC = os.path.join(WORK, "music")
CLOUD = bool(os.environ.get("GITHUB_ACTIONS"))

for p in (SERIES, os.path.dirname(os.path.abspath(__file__))):
    if p not in sys.path:
        sys.path.insert(0, p)
os.makedirs(OUTPUT, exist_ok=True)
