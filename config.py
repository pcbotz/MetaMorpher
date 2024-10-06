#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "21136840")
API_HASH = os.environ.get("API_HASH", "0f2ff6ef89fcd5ba226c3f40342f5319")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", '6719882299'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "pcott")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "pcleech")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Cluster0:Cluster0@cluster0.otkpn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002403233289')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://envs.sh/B-B.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '6719882299'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002113853127)
