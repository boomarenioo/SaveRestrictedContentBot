#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9058215
API_HASH = 59595a71c32a90d3fc061ad0bf9cd966
BOT_TOKEN = 5900683105:AAE7yotJmR7oidG9EVM9vaMPK2NswdrJyFc
SESSION = BAC6mTqun9ryQAwefmIHihnNeASV8SYjQhhKrz-wOmbNbehJYGO4zzlSVO8gdmYBITedDY7J7JTz2jtPcUr8OHRWVSPYFLamIC5HxDxsa5QzL37dqvaGerMFAMpwQBpfusWlugb587yJfMK7XvD5HgK0-AzBzDfsZKlWlkVVE1opqdmYJmbcf__u0wVpyZ10JuLqbjrA7acb_4jPzdLY7T_FOeQ5bI91XLtcC3604IxxgnbZhRYwT44ikaF5RxvxaWeuNHb3n3RACiq03lyyXTSBcXbILWoqM0Bci4VGUgf-0M92FNoE7TzhGEIkD_wZxFUuLcR59ZJ4Uiifw8CuF9tNKoi9kwA
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
