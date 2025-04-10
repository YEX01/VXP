import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
OWNER_ID = int(getenv("OWNER_ID", "6257927828"))
LOGGER_ID = int(getenv("LOGGER_ID", ""))

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/J9VX/VX7")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2d3fd5ccdd3d43dda6f17864d8eb7281")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "48d311d8910a4531ae81205e1f754d27")

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/ts1cz7.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/9077cd2ba5818efef2d28.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://graph.org/file/eb1e2b58e17964083db73.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://envs.sh/Ol4.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://envs.sh/Olr.jpg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://envs.sh/Olr.jpg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://envs.sh/Olk.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://files.catbox.moe/6xpaz5.jpg")
SOUNCLOUD_IMG_URL = "https://envs.sh/Olk.jpg"

SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/Olk.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/Olk.jpg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/Olk.jpg")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/storm_techh")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/storm_core")

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

def validate_url(url, url_type):
    if url and not re.match("(?:http|https)://", url):
        raise SystemExit(
            f"[ERROR] - Your {url_type} url is wrong. Please ensure that it starts with https://"
        )

validate_url(SUPPORT_CHANNEL, "SUPPORT_CHANNEL")
validate_url(SUPPORT_CHAT, "SUPPORT_CHAT")