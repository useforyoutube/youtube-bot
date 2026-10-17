"""Shared helpers for the render pipeline (the parts of the old bangla_toon.py that cine/thumbs use), made to run
on Windows (local) and Linux (GitHub Actions).
Text: Windows uses its own text engine (bn_text.ps1, shapes Devanagari/Bengali correctly); Linux uses Pillow's
Raqm layout with the Noto fonts (apt: fonts-noto-core, libraqm0)."""
import glob
import hashlib
import json
import os
import subprocess
import sys

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageFilter, ImageFont

from paths import ROOT, WORK  # noqa: F401  (re-exported for older code: bt.HERE)

HERE = WORK
SR = 24000
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
INK = (25, 20, 30)
WINDOWS = sys.platform == "win32"


def ease(p):
    p = min(1.0, max(0.0, p))
    return p * p * (3 - 2 * p)


def ease_back(p):
    p = min(1.0, max(0.0, p))
    c = 1.70158
    return 1 + (c + 1) * (p - 1) ** 3 + c * (p - 1) ** 2


# ---------------------------------------------------------------- text
TEXT_DIR = None
_masks = {}
_fonts = {}
FONT_DIRS = ["/usr/share/fonts/truetype/noto", "/usr/share/fonts/opentype/noto", "/usr/share/fonts/truetype/dejavu",
             os.path.join(ROOT, "fonts")]


def _find_font(names):
    for d in FONT_DIRS:
        for n in names:
            hit = glob.glob(os.path.join(d, "**", n), recursive=True)
            if hit:
                return hit[0]
    raise SystemExit(f"font not found: {names} (install fonts-noto-core)")


def _font_for(text, size):
    if any("\u0980" <= ch <= "\u09ff" for ch in text):
        names = ["NotoSansBengali-Bold.ttf", "NotoSerifBengali-Bold.ttf"]
    elif any("\u0900" <= ch <= "\u097f" for ch in text):
        names = ["NotoSansDevanagari-Bold.ttf", "NotoSerifDevanagari-Bold.ttf"]
    else:
        names = ["NotoSans-Bold.ttf", "DejaVuSans-Bold.ttf"]
    key = (names[0], size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(_find_font(names), size, layout_engine=ImageFont.Layout.RAQM)
    return _fonts[key]


def text_path(text, size):
    salt = "" if WINDOWS else "|linux2"          # bump when the Linux renderer changes, so old masks aren't reused
    return os.path.join(TEXT_DIR, hashlib.md5(f"{text}|{size}{salt}".encode()).hexdigest()[:14] + ".png")


def _script(ch):
    if "ऀ" <= ch <= "ॿ" or ch in "‌‍":
        return "deva"
    if "ঀ" <= ch <= "৿":
        return "beng"
    return "latin"


def _runs(line):
    """split a line into runs of one script each (spaces stay with the run they're in), so every run gets a font
    that has its glyphs - the Devanagari font has no '•', the Bengali font no Devanagari, etc."""
    runs = []
    for ch in line:
        sc = runs[-1][0] if ch == " " and runs else _script(ch)
        if runs and runs[-1][0] == sc:
            runs[-1][1] += ch
        else:
            runs.append([sc, ch])
    return runs


_SAMPLE = {"deva": "क", "beng": "ক", "latin": "A"}


def _render_linux(text, size, path):
    """white-on-black mask like the Windows engine makes; mixed scripts per line, lines centred"""
    from PIL import ImageDraw
    lines = text.split("\n")
    lh = int(size * 1.35)
    laid = []
    for ln in lines:
        parts = [(_font_for(_SAMPLE[sc], size), t) for sc, t in _runs(ln or " ")]
        laid.append((parts, sum(f.getlength(t) for f, t in parts)))
    asc = max(f.getmetrics()[0] for parts, _ in laid for f, _ in parts)
    w = int(max(lw for _, lw in laid)) + 24
    h = lh * len(lines) + int(size * 0.5) + 16
    im = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(im)
    for i, (parts, lw) in enumerate(laid):
        x = (w - lw) / 2
        for f, t in parts:
            d.text((x, 8 + i * lh + asc - f.getmetrics()[0]), t, font=f, fill=255)
            x += f.getlength(t)
    im.save(path)


def prepare_text(items):
    os.makedirs(TEXT_DIR, exist_ok=True)
    jobs = [dict(text=t, size=s, path=text_path(t, s)) for t, s in dict.fromkeys(items)
            if not os.path.exists(text_path(t, s))]
    if not jobs:
        return
    if WINDOWS:
        job_file = os.path.join(TEXT_DIR, "jobs.json")
        with open(job_file, "w", encoding="utf-8") as f:
            json.dump(jobs, f, ensure_ascii=False)
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                        os.path.join(os.path.dirname(os.path.abspath(__file__)), "bn_text.ps1"), job_file], check=True)
    else:
        for j in jobs:
            _render_linux(j["text"], j["size"], j["path"])


def mask(text, size, stroke=0):
    key = (text, size, stroke)
    if key not in _masks:
        m = Image.open(text_path(text, size)).convert("L")
        bbox = m.getbbox()
        m = m.crop(bbox) if bbox else m
        if stroke:
            pad = stroke + 2
            big = Image.new("L", (m.width + 2 * pad, m.height + 2 * pad), 0)
            big.paste(m, (pad, pad))
            m = big.filter(ImageFilter.MaxFilter(2 * stroke + 1))
        _masks[key] = m
    return _masks[key]


def put_text(img, text, size, cx, cy, fill, stroke=0, stroke_fill=INK, scale=1.0):
    if scale <= 0.05:
        return
    layers = ([(mask(text, size, stroke), stroke_fill)] if stroke else []) + [(mask(text, size), fill)]
    for m, col in layers:
        if scale != 1.0:
            m = m.resize((max(1, int(m.width * scale)), max(1, int(m.height * scale))), Image.BILINEAR)
        x0, y0 = int(cx - m.width / 2), int(cy - m.height / 2)
        img.paste(col, (x0, y0, x0 + m.width, y0 + m.height), m)


WRAP = [40]


def wrap(text, maxc=None):
    maxc = maxc or WRAP[0]
    if "\n" in text:
        return text
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > maxc:
            lines.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    return "\n".join(lines + [cur])


_efonts = {}


def efont(size):
    """Latin font for small labels (copyright line)"""
    if size not in _efonts:
        path = r"C:\Windows\Fonts\arialbd.ttf" if WINDOWS else _find_font(["NotoSans-Bold.ttf", "DejaVuSans-Bold.ttf"])
        _efonts[size] = ImageFont.truetype(path, size)
    return _efonts[size]


# ---------------------------------------------------------------- audio
def load_audio(path):
    raw = subprocess.run([FFMPEG, "-v", "error", "-i", path, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def add_tone(out, t0, midi, dur, vol, decay, harm=0.3):
    f = 440 * 2 ** ((midi - 69) / 12)
    s = int(t0 * SR)
    n = min(int(dur * SR), len(out) - s)
    if n <= 0 or s < 0:
        return
    tt = np.arange(n, dtype=np.float32) / SR
    w = np.sin(2 * np.pi * f * tt) + harm * np.sin(4 * np.pi * f * tt)
    out[s:s + n] += (w * np.exp(-tt * decay) * np.minimum(1, tt / 0.01) * vol).astype(np.float32)


def sfx(name):
    rng = np.random.default_rng(5)
    if name == "chime":
        out = np.zeros(int(1.4 * SR), np.float32)
        for k, m in enumerate((84, 88, 91, 96)):
            add_tone(out, k * 0.08, m, 1.0, 0.07, 3)
        return out
    if name == "thunder":
        n = int(3.0 * SR)
        tt = np.arange(n, dtype=np.float32) / SR
        noise = np.convolve(rng.uniform(-1, 1, n).astype(np.float32), np.ones(120, np.float32) / 120, "same")
        return noise * np.exp(-tt * 1.2) * np.minimum(1, tt / 0.05) * 6
    if name == "gong":
        out = np.zeros(int(3.5 * SR), np.float32)
        for m, v in ((45, 0.25), (57, 0.12), (64, 0.06)):
            add_tone(out, 0, m, 3.5, v, 0.9, harm=0.5)
        return out
    return np.zeros(1, np.float32)
