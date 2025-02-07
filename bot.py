# Hey Give Me Star 🥲



import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import logging
from plugins.config import Config
from pyrogram import Client as Ntbots
from pyrogram import filters

# Set logging level
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Fix indentation issue
if not os.path.isdir(Config.DOWNLOAD_LOCATION):  
    os.makedirs(Config.DOWNLOAD_LOCATION)

plugins = dict(root="plugins")

# Initialize Pyrogram client
Ntbots = Ntbots(
    "UploadLinkToFileBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)

print("🎊 I AM ALIVE 🎊  • Support ")
Ntbots.run()
