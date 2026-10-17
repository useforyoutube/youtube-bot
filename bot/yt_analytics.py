"""Daily channel report from YouTube Analytics (read-only, its own token - uploads keep youtube_token.json).
    python yt_analytics.py            # report for the Kalki videos (last 28 days + per video)
    python yt_analytics.py --days 7
First run opens the browser once to approve read-only Analytics access."""
import json
import os
import sys
from datetime import date, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

HERE = os.path.dirname(os.path.abspath(__file__))
SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly", "https://www.googleapis.com/auth/youtube.readonly"]
TOKEN = os.path.join(HERE, "youtube_analytics_token.json")
CLIENT_SECRET = os.path.join(HERE, "client_secret.json")


def creds():
    c = Credentials.from_authorized_user_file(TOKEN, SCOPES) if os.path.exists(TOKEN) else None
    if not c or not c.valid:
        if c and c.expired and c.refresh_token:
            c.refresh(Request())
        else:
            c = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES).run_local_server(port=0)
        with open(TOKEN, "w") as f:
            f.write(c.to_json())
    return c


def kalki_ids():
    pub = json.load(open(os.path.join(HERE, "published.json")))
    return {k: v for k, v in pub.items() if k.startswith("kalki")}


def report(days=28):
    c = creds()
    ya = build("youtubeAnalytics", "v2", credentials=c)
    yt = build("youtube", "v3", credentials=c)
    end, start = date.today(), date.today() - timedelta(days=days)
    q = dict(ids="channel==MINE", startDate=str(start), endDate=str(end))
    out = {"period": f"{start} -> {end}"}

    ch = ya.reports().query(**q, metrics="views,estimatedMinutesWatched,averageViewDuration,subscribersGained,"
                                          "subscribersLost").execute()
    out["channel"] = dict(zip([h["name"] for h in ch["columnHeaders"]], (ch.get("rows") or [[0] * 5])[0]))

    ids = kalki_ids()
    vids = {}
    if ids:
        r = ya.reports().query(**q, dimensions="video", filters="video==" + ",".join(ids.values()),
                               metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,"
                                       "likes,comments,shares,subscribersGained").execute()
        cols = [h["name"] for h in r["columnHeaders"]]
        for row in r.get("rows", []):
            vids[row[0]] = dict(zip(cols[1:], row[1:]))
        names = {it["id"]: it["snippet"]["title"] for it in
                 yt.videos().list(part="snippet", id=",".join(ids.values())).execute()["items"]}
        out["videos"] = [{"key": k, "id": v, "title": names.get(v, ""), **vids.get(v, {})} for k, v in ids.items()]

    r = ya.reports().query(**q, dimensions="insightTrafficSourceType", metrics="views", sort="-views").execute()
    out["traffic_sources"] = r.get("rows", [])
    r = ya.reports().query(**q, dimensions="video", metrics="views,estimatedMinutesWatched,averageViewPercentage",
                           sort="-views", maxResults=10).execute()
    top = r.get("rows", [])
    if top:
        t = {it["id"]: it["snippet"]["title"] for it in
             yt.videos().list(part="snippet", id=",".join(x[0] for x in top)).execute()["items"]}
        out["top_videos"] = [dict(title=t.get(x[0], ""), id=x[0], views=x[1], minutes=x[2], pct_watched=x[3]) for x in top]
    r = ya.reports().query(**q, dimensions="insightTrafficSourceDetail", filters="insightTrafficSourceType==YT_SEARCH",
                           metrics="views", sort="-views", maxResults=15).execute()
    out["search_terms"] = r.get("rows", [])
    out["note"] = "Thumbnail impressions / click rate are only in YouTube Studio (not in the API)."
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 28
    print(json.dumps(report(days), ensure_ascii=False, indent=2))
