# youtube-bot

An automated YouTube video pipeline that runs entirely on GitHub Actions.

**The bot's code, scripts and data are encrypted** in `vault.enc` and can only be unlocked by a scheduled run
that holds the owner's `REPO_KEY` secret. The files you can see here (the workflow definitions and this small
`vault/boot.py` helper) only unlock and run the bot; they contain no code logic and no secrets.

Downloading this repository gives you an encrypted blob that is useless without the owner's key.

© 2026 Sujay Ganguly Creations. All rights reserved.
