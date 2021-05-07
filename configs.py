# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [【◉ LIBRARIAN'S STORE ROOM◉】](https://t.me/{BOT_USERNAME})

📝 **Programing Language:** [🐍Python 3.9.5 ](https://www.python.org/downloads/release/python-395/)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developers:**

__**[🐍PURUSHOTTAM MAHAJAN🐍](https://t.me/Purushottam_Mahajan)**__

__**[😼ANIMESH VERMA😼](https://t.me/AniMesH941)**__

👥 **【◉ ALL ABOUT DEVLOPERS ◉】:** 
[【◉Librarian Networks◉】](https://t.me/Team_Librarian/57)

📢 **【◉ For Enterance Exams◉】:**
 [【◉SCIENCE WALE◉】](https://t.me/Science_Wale)
 
 🤓 **【◉For MH-BOARDS ◉】:**
 [【◉LIBRARIAN OFFICIAL◉】](htps://t.me/Librarian_Offficial)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developers:**

__**[🐍PURUSHOTTAM MAHAJAN🐍](https://t.me/Purushottam_Mahajan)**___

__**[😼ANIMESH VERMA😼](https://t.me/AniMesH941)**__


Developers is Super Noob. Just Learning from Official Docs. Please Donate / And Support the developer fors Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[😉DONATE NOW🥺](https://t.me/Purushottam_Mahajan) (ASK HIM FOR UOW TO PAY 😅)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
