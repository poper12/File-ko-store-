import os
import logging
from logging.handlers import RotatingFileHandler

settings = {
    '_id': 1,  # don't change this line only, if you do you're dying by my hand
    "SPOILER": True,  # bool write True or False
    "FILE_AUTO_DELETE": 3600,  # in seconds
    "AUTO_DEL": True,  # bool write True or False
    "STICKER_ID": "CAACAgUAAyEFAASAgUwqAAJh_mckw2STkeY1WMOHJGY4Hs9_1-2fAAIPFAACYLShVon-N6AFLnIiHgQ",
    "stk_del_timer": 1, # in seconds
    "bot_admin": [2093552866] #e.g. 1963929292,38739292827 differetiate admins with a comma
}

HELP_MSG = """help msg
"""  # shown only to admins

# Bot token @Botfather
TG_BOT_TOKEN = '7717441829:AAHNhP853L6wFR13-vqG5nlDECq5J1xKl3c'
# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25262375"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e3140fb33bad778f0ca42e0d36ec13a")

# Your db channel Id
DB_CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002432294589"))

# NAME OF OWNER
OWNER = os.environ.get("OWNER", "NOIR")

# OWNER ID
OWNER_ID = 5543390445

# SUDO: those who can edit admins in channel
SUDO = [2093552866]
if OWNER_ID not in SUDO:
    SUDO.append(OWNER_ID)

# Port
PORT = os.environ.get("PORT", "8108")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://userbot:userbot@cluster0.iweqz.mongodb.net/test?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Noir1")

# FSUBS configuration
FSUBS = [
    {'_id': -1002084570715, "CHANNEL_NAME": "Anime NOIR"}
]


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>ʏᴏᴏ {mention} ✌🏻</b></blockquote> <blockquote>ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋꜱ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</blockquote>")
ADMINS = []
# Add other admin IDs here as needed, ensuring not to include OWNER_ID
other_admin_ids = []  # Replace with actual admin IDs
for admin_id in other_admin_ids:
    if admin_id != OWNER_ID:
        ADMINS.append(admin_id)

# Ensure OWNER_ID is not duplicated
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = '<blockquote expandable><b>{previouscaption}</b></blockquote>'

# Set True if you want to prevent users from forwarding files from the bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want to disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = True  # True or None

BOT_STATS_TEXT = "<blockquote><b>BOT UPTIME</b>\n{uptime}</blockquote>"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
