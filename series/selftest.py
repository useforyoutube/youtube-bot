"""Bot self-test: a ~25 s video made only from library pictures. Exercises Hindi/English text, voices, music
download, the face/mouth detector, rendering and the thumbnail - but is never uploaded.
Used by `run.py --selftest` and as the safety gate for automatic code repairs."""
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT

SERIES = "सेल्फ़ टेस्ट • भाग 1"
PLAYLIST = None
HOOK = "बॉट टेस्ट"
HOOK2 = "हिंदी • English • বাংলা"
NEXT = "सब ठीक है"
VOICES = {"N": ("hi-IN-MadhurNeural", "-10%", "-8Hz", "narrator"),
          "Kalki": ("hi-IN-MadhurNeural", "-4%", "+0Hz", "soft")}
SPEAKERS = {"Kalki": ("कल्कि", (255, 214, 120))}
TALK = {}
IMAGES = [("golden_shambhala", None), ("kalki_young_face", None), ("kali_face", None)]
LINES = [
    ("#", "शुरुआत"),
    (["golden_shambhala"], "N", "यह बॉट का एक छोटा सा परीक्षण है... आवाज़, संगीत और चित्र।", ""),
    (["kalki_young_face"], "Kalki", "अगर आप मेरी आवाज़ सुन रहे हैं... तो सब ठीक है।", ""),
    ("#", "अंत"),
    (["kali_face"], "N", "परीक्षण पूरा हुआ।", "thunder"),
]
MUSIC_PLAN = [(0.0, "Heroic Age.mp3", 0.0)]
MUSIC_CREDIT = '"Heroic Age" - Kevin MacLeod (incompetech.com). Licensed under CC BY 4.0'
THUMB2 = dict(hero=("kalki_young_face", 0.5), other=("kali_face", 0.5), big="बॉट टेस्ट!", small="सब ठीक है", badge="टेस्ट")
SEO = dict(title="self test", description="self test {CHAPTERS} {MUSIC_CREDIT} {DISCLAIMER}", tags=["test"],
           categoryId="24")
SHORTS = []
