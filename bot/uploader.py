"""YouTube upload for the cloud bot. Never sleeps: a video is uploaded as private with a publishAt time in the next
free prime-time slot (YouTube publishes it on time by itself), or QuotaWait is raised so the run stops and the next
run continues after the daily reset (midnight US Pacific = 12:30 IST).
Login: env YT_TOKEN (authorized-user JSON with refresh_token) + YT_CLIENT_SECRET, or state-free local files."""
import datetime
import json
import os
from zoneinfo import ZoneInfo

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from paths import ROOT, STATE

SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/yt-analytics.readonly"]
LEDGER = os.path.join(STATE, "quota_ledger.json")
SCHEDULE = os.path.join(STATE, "publish_schedule.json")
PUBLISHED = os.path.join(STATE, "published.json")
CAP = 9000                                   # of the 10,000 free units a day
COST = {"upload": 1600, "thumb": 50, "update": 50, "list": 1, "comment": 50, "playlist": 50}
SLOTS_IST = {"long": ["12:30", "19:00", "21:00"], "short": ["08:00", "12:00", "16:30"]}
IST = ZoneInfo("Asia/Kolkata")


class QuotaWait(Exception):
    """Daily YouTube quota is used up: stop now, continue after the reset."""


def _load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def credentials():
    info = os.environ.get("YT_TOKEN")
    info = json.loads(info) if info else _load(os.path.join(ROOT, "youtube_token.json"), None)
    if not info:
        raise SystemExit("No YouTube login (YT_TOKEN secret missing)")
    c = Credentials.from_authorized_user_info(info)
    if not c.valid:
        c.refresh(Request())                    # uses the permanent refresh token; nothing is written back
    return c


def service():
    return build("youtube", "v3", credentials=credentials(), cache_discovery=False)


# ---------------------------------------------------------------- quota (resets at midnight US Pacific)
def pt_day():
    return datetime.datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()


def used():
    return _load(LEDGER, {}).get(pt_day(), 0)


def spend(units, set_to=None):
    week_ago = (datetime.date.fromisoformat(pt_day()) - datetime.timedelta(days=7)).isoformat()
    data = {k: v for k, v in _load(LEDGER, {}).items() if k >= week_ago}
    data[pt_day()] = set_to if set_to is not None else data.get(pt_day(), 0) + units
    _save(LEDGER, data)


def need(units):
    if used() + units > CAP:
        raise QuotaWait(f"YouTube quota: {used()} used today, need {units}")


def guard(call, units):
    """run an API call, spending its units; a quota error from YouTube means: stop until the reset"""
    need(units)
    try:
        r = call()
    except HttpError as e:
        if "quota" in str(e).lower():
            spend(0, set_to=10000)
            raise QuotaWait(str(e)[:200])
        raise
    spend(units)
    return r


# ---------------------------------------------------------------- slots
def next_slot(kind, min_lead_minutes=60, not_before=None):
    """earliest free slot; a long video always goes AFTER every long slot already booked (episodes stay in order)"""
    booked = set(_load(SCHEDULE, []))
    now = datetime.datetime.now(IST)
    floor = now + datetime.timedelta(minutes=min_lead_minutes)
    if kind == "long":
        longs = [datetime.datetime.fromisoformat(b) for b in booked
                 if datetime.datetime.fromisoformat(b).strftime("%H:%M") in SLOTS_IST["long"]]
        if longs:
            floor = max(floor, max(longs) + datetime.timedelta(minutes=1))
    if not_before:
        floor = max(floor, not_before + datetime.timedelta(minutes=1))
    day = floor.date()
    while True:
        for hm in SLOTS_IST[kind]:
            h, m = map(int, hm.split(":"))
            slot = datetime.datetime(day.year, day.month, day.day, h, m, tzinfo=IST)
            if slot >= floor and slot.isoformat() not in booked:
                keep = {b for b in booked if b >= (now - datetime.timedelta(days=3)).isoformat()}
                _save(SCHEDULE, sorted(keep | {slot.isoformat()}))
                return slot
        day += datetime.timedelta(days=1)


def check_meta(meta):
    assert len(meta["title"]) <= 100, f"title is {len(meta['title'])} chars (max 100)"
    assert "<" not in meta["title"] + meta["description"], "YouTube rejects '<' and '>'"
    assert len(meta["description"].encode()) <= 5000, "description over 5000 bytes"
    tag_len = sum(len(t) + (2 if " " in t else 0) + 1 for t in meta["tags"])
    assert tag_len <= 500, f"tags total {tag_len} chars (max ~500)"


def published():
    return _load(PUBLISHED, {})


def find_upload(text):
    """is a video whose title contains `text` on the channel yet? -> (id, publish time) or None (2-3 quota units)"""
    yt = service()
    ch = guard(lambda: yt.channels().list(part="contentDetails", mine=True).execute(), COST["list"])
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    items = guard(lambda: yt.playlistItems().list(part="snippet", playlistId=uploads, maxResults=50).execute(),
                  COST["list"]).get("items", [])
    for it in items:
        if text in it["snippet"]["title"]:
            vid = it["snippet"]["resourceId"]["videoId"]
            st = guard(lambda: yt.videos().list(part="status", id=vid).execute(), COST["list"])["items"][0]["status"]
            at = st.get("publishAt")
            when = (datetime.datetime.fromisoformat(at.replace("Z", "+00:00")) if at
                    else datetime.datetime.now(datetime.timezone.utc))
            return vid, when.astimezone(IST)
    return None


def upload(key, video, meta, kind, thumbnail=None, not_before=None):
    """Upload `video` (scheduled into the next `kind` slot). Returns the video id; records it under `key`."""
    pub = published()
    if key in pub:
        return pub[key]
    check_meta(meta)
    need(COST["upload"] + COST["thumb"] + COST["playlist"] + 10)
    yt = service()
    at = next_slot(kind, not_before=not_before)
    body = {"snippet": {k: meta[k] for k in ("title", "description", "tags", "categoryId", "defaultLanguage",
                                             "defaultAudioLanguage")},
            "status": {"privacyStatus": "private", "publishAt": at.astimezone(datetime.timezone.utc)
                       .strftime("%Y-%m-%dT%H:%M:%SZ"), "selfDeclaredMadeForKids": meta["madeForKids"],
                       "containsSyntheticMedia": meta["containsSyntheticMedia"]}}
    media = MediaFileUpload(video, mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)

    def run():
        resp = None
        while resp is None:
            _, resp = req.next_chunk()
        return resp
    vid = guard(run, COST["upload"])["id"]
    pub[key] = vid
    _save(PUBLISHED, pub)
    print(f"uploaded {key}: https://youtu.be/{vid} (goes public {at:%a %d %b %H:%M} IST)", flush=True)
    if thumbnail and os.path.exists(thumbnail):
        try:
            guard(lambda: yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(thumbnail)).execute(),
                  COST["thumb"])
        except HttpError as e:
            print("thumbnail failed:", str(e)[:200])
    if meta.get("playlistId"):
        try:
            guard(lambda: yt.playlistItems().insert(part="snippet", body={"snippet": {
                "playlistId": meta["playlistId"], "resourceId": {"kind": "youtube#video", "videoId": vid}}}).execute(),
                COST["playlist"])
        except HttpError as e:
            print("playlist add failed:", str(e)[:200])
    media.stream().close()
    return vid


def verify(vid, meta):
    """after-upload check: fix title/description/tags if YouTube stored something different"""
    yt = service()
    items = guard(lambda: yt.videos().list(part="snippet,status", id=vid).execute(), COST["list"]).get("items")
    if not items:
        return False
    s = items[0]["snippet"]
    if s.get("title") != meta["title"] or s.get("description") != meta["description"]:
        sn = {k: meta[k] for k in ("title", "description", "tags", "categoryId", "defaultLanguage",
                                   "defaultAudioLanguage")}
        guard(lambda: yt.videos().update(part="snippet", body={"id": vid, "snippet": sn}).execute(), COST["update"])
    return True
