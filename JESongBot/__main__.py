#Uvindu Bro <https://t.me/UvinduBro>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm powerful  Song Downloader Bot 🎵 By @dexter119 \n\nMade With ❤️ In Sri Lanka 🇱🇰

😉 Just send me the song name you want to download.😋
      eg:```/song Childhood```
      
A bot by @dexter119 🇱🇰
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel 🔊", url="https://t.me/m_u_s_i_c_f_a_n_s"
                    ),
                    InlineKeyboardButton(
                        text="Dev 🔥", url="https://t.me/dexter119"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ mySongBot is online.")
idle()
