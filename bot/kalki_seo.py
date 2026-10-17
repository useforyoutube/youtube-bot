"""SEO kit for the Kalki series, built from the tags/titles of the top Kalki & Kaliyug videos on YouTube
(The Divine Tales 1 cr, Vedic Vatika 80 L, Kalki Puran audiobook 68 L, Gehre Shabd 50 L, Rahasya Dharm, Vaikuntha
Films, RAAAZ, Hari Universe...). Patterns: question/fear first, Hindi + English, 'Full Story', 'Part N';
tags cover every spelling people search (kalyug/kaliyug/kaliyuga, avatar/avtar, puran/purana)."""

CORE_TAGS = [
    "kalki avatar", "kalyug ka ant", "kaliyug ka ant kaise hoga", "kalyug ka ant kab hoga", "kalki puran",
    "kalki avatar story in hindi", "kalki vs kali", "kalki", "kaliyug", "kalyug", "kaliyuga", "end of kaliyuga",
    "kalki avtar", "kalki purana", "kali purush", "shambhala", "kalki 2898 ad", "yug parivartan",
    "vishnu 10th avatar", "hindu mythology", "कल्कि अवतार", "कलियुग का अंत", "कल्कि पुराण", "कलयुग",
]
HASHTAGS = "#kalki #kalkiavatar #kaliyug #kalkipuran #hindumythology #vishnu #sanatandharma #hinduism #mahabharat"
SHORT_HASHTAGS = "#shorts #kalki #kalkiavatar #kaliyug #hindumythology #sanatan"


def tags(extra):
    """Episode-specific tags first, then the core pool; YouTube's 500-char limit (quoted multi-word tags)."""
    out, total = [], 0
    for t in dict.fromkeys(extra + CORE_TAGS):
        cost = len(t) + (2 if " " in t else 0) + 1
        if total + cost <= 490:
            out.append(t)
            total += cost
    return out


def description(hook_line, story, english, ep, total_eps=15):
    return f"""{hook_line}

{story}

{english}

📺 कल्कि सीरीज़ - भाग {ep} / {total_eps}

⏱️ अध्याय / Chapters
{{CHAPTERS}}

🔔 अगला भाग मिस न करें: चैनल को सब्सक्राइब करें और बेल आइकन दबाएँ!
📤 इस वीडियो को अपने परिवार और दोस्तों के साथ शेयर करें।
💬 कमेंट में लिखिए... जय श्री कल्कि! 🙏

⚠️ Disclaimer: {{DISCLAIMER}}

🎵 Music: {{MUSIC_CREDIT}}

{HASHTAGS}

© 2026 Sujay Ganguly Creations. All rights reserved. Story adaptation, script, artwork and video are by Sujay Ganguly Creations. Re-uploading or copying this video without permission is strictly prohibited."""


def short_description(hook_line):
    return f"""{hook_line}

🎬 पूरा एपिसोड: {{FULL_EPISODE}}
🔔 पूरी कहानी के लिए चैनल को सब्सक्राइब करें और शेयर करें!

⚠️ {{DISCLAIMER}}
🎵 Music: {{MUSIC_CREDIT}}

{SHORT_HASHTAGS}

© 2026 Sujay Ganguly Creations. All rights reserved."""
