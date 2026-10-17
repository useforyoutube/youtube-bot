"""Quiet hours: no rendering, uploading or API work between 08:00 and 16:00 (local India time), Mon-Fri.
Saturday and Sunday run normally."""
import datetime
import os
import time

QUIET_START = datetime.time(8, 0)
QUIET_END = datetime.time(16, 0)


def in_quiet(now=None):
    if os.environ.get("GITHUB_ACTIONS"):          # quiet hours protect the home PC only
        return False
    now = now or datetime.datetime.now()
    return now.weekday() < 5 and QUIET_START <= now.time() < QUIET_END     # Mon=0 .. Fri=4


def wait_if_quiet(label=""):
    """Block (idle, no CPU) until quiet hours are over."""
    if not in_quiet():
        return
    end = datetime.datetime.combine(datetime.date.today(), QUIET_END)
    print(f"[quiet hours] pausing {label} until {end.strftime('%H:%M')}...", flush=True)
    while in_quiet():
        time.sleep(60)
    print(f"[quiet hours] resuming {label}", flush=True)
