"""Pictures for a series module: FLUX.1-schnell on Cloudflare Workers AI (free daily allowance).
Library pictures (prompt None) are copied from the committed character library or an earlier episode.
    python myth_images.py <module>
Exit codes: 0 = all pictures ready, 3 = daily free limit reached (wait for the 00:00 UTC reset),
            1 = other error. Never sleeps on the limit, so no GitHub minutes are wasted."""
import base64
import importlib
import io
import json
import os
import shutil
import sys
import time

import requests
from PIL import Image

from paths import LIBRARY, OUTPUT, ROOT
from quiet import wait_if_quiet

STYLE = (", traditional Hindu devotional painting, divine glowing halo, ornate gold jewelry, rich vibrant colors, "
         "cinematic lighting, highly detailed, sacred atmosphere, no text, no letters, no signature, no watermark")
MODEL = "@cf/black-forest-labs/flux-1-schnell"
LIMIT = 3


class DailyLimit(Exception):
    pass


def creds():
    if os.environ.get("CF_ACCOUNT_ID"):
        return os.environ["CF_ACCOUNT_ID"], os.environ["CF_TOKEN"]
    cfg = json.load(open(os.path.join(ROOT, "cloudflare.json")))           # local runs only (never committed)
    return cfg["account_id"], cfg["token"]


def cloudflare(prompt, path):
    acc, tok = creds()
    r = requests.post(f"https://api.cloudflare.com/client/v4/accounts/{acc}/ai/run/{MODEL}",
                      headers={"Authorization": f"Bearer {tok}"},
                      json=dict(prompt=prompt + ", subject centered, full figure in the middle of the frame", steps=4),
                      timeout=120)
    if r.status_code == 429 or (r.status_code >= 400 and "neuron" in r.text.lower()):
        raise DailyLimit(r.text[:200])
    r.raise_for_status()
    Image.open(io.BytesIO(base64.b64decode(r.json()["result"]["image"]))).convert("RGB").save(path, quality=90)


def library_source(key):
    for p in [os.path.join(LIBRARY, f"{key}.jpg")] + [
            os.path.join(OUTPUT, d, "img", f"{key}.jpg") for d in sorted(os.listdir(OUTPUT))]:
        if os.path.exists(p):
            return p
    return None


def generate(name):
    m = importlib.import_module(name)
    out = os.path.join(OUTPUT, name, "img")
    os.makedirs(out, exist_ok=True)
    made = 0
    for key, prompt in m.IMAGES:
        path = os.path.join(out, f"{key}.jpg")
        if os.path.exists(path):
            continue
        if prompt is None:
            src = library_source(key)
            if not src:
                raise SystemExit(f"library picture not found: {key}")
            shutil.copy(src, path)
            continue
        for attempt in range(4):
            wait_if_quiet("image generation")
            try:
                cloudflare(prompt + getattr(m, "STYLE", STYLE), path)
                made += 1
                print("image", key, flush=True)
                break
            except DailyLimit as e:
                print(f"daily picture limit reached after {made} new pictures: {e}", flush=True)
                sys.exit(LIMIT)
            except Exception as e:                     # network blip: short retry
                print("retry", key, str(e)[:160], flush=True)
                time.sleep(15 * (attempt + 1))
        else:
            raise SystemExit(f"could not generate {key}")
    print(f"all pictures ready for {name} ({made} new)", flush=True)


if __name__ == "__main__":
    import paths  # noqa: F401  (puts series/ on sys.path)
    generate(sys.argv[1])
