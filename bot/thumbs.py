"""Hero-vs-villain thumbnails for the Kalki series: hero (warm, bright) on the left, the other side on the right,
a glowing gold seam between them, 2-4 big words and a red 'भाग N' badge. Uses library pictures only.
    python thumbs.py kalki01 [kalki02 ...]           -> output/<ep>/thumbnail.jpg (+ a copy in output/thumbs/)
    python thumbs.py --set kalki01 kalki02 ...        also replaces the thumbnail on YouTube (published episodes)"""
import glob
import importlib
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import toolkit as bt
from paths import LIBRARY, OUTPUT, STATE

W, H = 1920, 1080
GOLD, WHITE, RED = (255, 214, 60), (255, 255, 255), (200, 20, 30)
COPY = "© 2026 Sujay Ganguly Creations"

# hero picture, right-side picture, big line, small line   (focus = horizontal centre of the subject, 0..1)
DESIGN = {
    "kalki01": dict(hero=("kalki_young_face", 0.5), other=("kali_face", 0.5), big="कलि काँप उठा!", small="कल्कि का जन्म"),
    "kalki02": dict(hero=("kalki_sword_raise", 0.45), other=("vikoka", 0.5), big="पहला युद्ध!", small="परशुराम की शिक्षा"),
    "kalki03": dict(hero=("kalki_young_face", 0.5), other=("shiva_face", 0.5), big="महादेव का वरदान!",
                    small="3 दिव्य उपहार", other_tone="divine"),
    "kalki04": dict(hero=("padmavati_face", 0.5), other=("kings_transform", 0.5), big="राजा बन गए स्त्री!",
                    small="पद्मावती का रहस्य", other_tone="divine"),
    "kalki05": dict(hero=("kalki_smile", 0.5), other=("padmavati_face", 0.5), big="श्राप टूट गया!",
                    small="कल्कि और पद्मावती", other_tone="divine"),
    "kalki06": dict(hero=("kalki_fight_kings", 0.55), other=("kali_rage", 0.45), big="पहला धर्मयुद्ध!",
                    small="काली विद्या vs आग्नेयास्त्र"),
    "vishnu24": dict(hero=("vishnu_glow", 0.5), other=("a15_narasimha", 0.5), big="विष्णु के 24 अवतार",
                     small="सनकादि से कल्कि तक", other_tone="divine", badge="पूरी कथा"),
    "kalki07": dict(hero=("kalki", 0.45), other=("koka_vikoka", 0.5), big="मरकर भी ज़िंदा!", small="कोक-विकोक का अंत"),
}


def find(key):
    hits = sorted(glob.glob(os.path.join(LIBRARY, f"{key}.jpg")) +
                  glob.glob(os.path.join(OUTPUT, "*", "img", f"{key}.jpg")))
    if not hits:
        raise SystemExit(f"picture not found: {key}")
    return Image.open(hits[0]).convert("RGB")


def crop(im, w, h, focus):
    """cover-crop to w x h keeping the subject (horizontal focus) in frame"""
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s + 0.5), int(im.height * s + 0.5)), Image.LANCZOS)
    x = int(min(max(focus * im.width - w / 2, 0), im.width - w))
    y = int((im.height - h) * 0.25)
    return im.crop((x, y, x + w, y + h))


def tone(im, kind):
    im = ImageEnhance.Color(im).enhance(1.35)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    a = np.asarray(im).astype(np.float32)
    if kind == "hero":                      # warm and bright
        a = a * [1.10, 1.02, 0.90] + 12
    elif kind == "villain":                 # dark, purple-red
        a = a * [1.05, 0.80, 1.10] * 0.92
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def design(ep):
    """thumbnail design: listed here, or THUMB2 = dict(hero=..., other=..., big=..., small=...) in the episode file"""
    if ep in DESIGN:
        return DESIGN[ep]
    try:
        return getattr(importlib.import_module(ep), "THUMB2", None)
    except ImportError:
        return None


def make(ep):
    d = design(ep)
    m = importlib.import_module(ep)
    bt.TEXT_DIR = os.path.join(OUTPUT, ep, "text_cache")
    badge = d.get("badge") or f"भाग {m.SERIES.split()[-1]}"
    bt.prepare_text([(d["big"], 170), (d["small"], 96), (badge, 70)])

    split = int(W * 0.56)
    left = tone(crop(find(d["hero"][0]), split + 120, H, d["hero"][1]), "hero")
    right = tone(crop(find(d["other"][0]), W - split + 120, H, d["other"][1]), d.get("other_tone", "villain"))
    canvas = Image.new("RGB", (W, H))
    canvas.paste(right, (split - 120, 0))
    # diagonal seam: hero covers the left, edge slanted, soft gold glow along it
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    edge = split + (yy / H - 0.5) * 220                      # slant
    hero_mask = np.clip((edge - xx) / 6 + 0.5, 0, 1)
    full_left = Image.new("RGB", (W, H))
    full_left.paste(left, (0, 0))
    a = np.asarray(full_left).astype(np.float32) * hero_mask[..., None] + \
        np.asarray(canvas).astype(np.float32) * (1 - hero_mask[..., None])
    glow = np.exp(-((xx - edge) / 10) ** 2)[..., None] * np.array([255, 200, 80]) * 0.95 + \
        np.exp(-((xx - edge) / 45) ** 2)[..., None] * np.array([255, 150, 30]) * 0.35
    a = a + glow
    a *= (1 - 0.55 * np.clip((yy / H - 0.55) / 0.45, 0, 1))[..., None]      # darken the bottom for the text
    a *= (1 - 0.25 * np.clip(1 - yy / (H * 0.18), 0, 1))[..., None]
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

    def fit(t, s, st):
        return min(1.0, 0.94 * W / bt.mask(t, s, st).width)
    bt.put_text(im, d["big"], 170, W / 2, H - 290, GOLD, stroke=14, stroke_fill=(0, 0, 0), scale=fit(d["big"], 170, 14))
    bt.put_text(im, d["small"], 96, W / 2, H - 92, WHITE, stroke=10, stroke_fill=(0, 0, 0),
                scale=fit(d["small"], 96, 10))
    # badge, top-left
    bm = bt.mask(badge, 70)
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((40, 36, 40 + bm.width + 60, 36 + bm.height + 44), radius=18, fill=RED, outline=WHITE, width=4)
    bt.put_text(im, badge, 70, 40 + (bm.width + 60) / 2, 36 + (bm.height + 44) / 2, WHITE)
    dr.text((W - 24, 22), COPY, font=bt.efont(30), fill=WHITE, anchor="ra", stroke_width=3, stroke_fill=(20, 15, 15))

    out = im.resize((1280, 720), Image.LANCZOS)
    path = os.path.join(OUTPUT, ep, "thumbnail.jpg")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out.save(path, quality=92)
    os.makedirs(os.path.join(OUTPUT, "thumbs"), exist_ok=True)
    out.save(os.path.join(OUTPUT, "thumbs", f"{ep}.jpg"), quality=92)
    return path


def set_on_youtube(ep, path):
    import uploader as u
    from googleapiclient.http import MediaFileUpload
    vid = json.load(open(os.path.join(STATE, "published.json"))).get(ep)
    if not vid:
        print(ep, "not published yet - thumbnail will be used at upload")
        return
    yt = u.service()
    u.guard(lambda: yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(path)).execute(), u.COST["thumb"])
    print(ep, "thumbnail replaced on YouTube:", vid)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    eps = [a for a in sys.argv[1:] if not a.startswith("--")]
    for ep in eps:
        p = make(ep)
        print("made", p)
        if "--set" in sys.argv:
            set_on_youtube(ep, p)
