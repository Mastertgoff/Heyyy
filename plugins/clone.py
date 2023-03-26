from pyrogram import Client, filters, enums
from info import ADMINS, API_ID, API_HASH
import re
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
#from utlis import clone_temp
from database.clone_botsdb import db

@Client.on_message(filters.command("clone") & filters.user(ADMINS))
async def delvarrrssz(bot, message):
    msg = await message.reply_text("Proccesing.. ")
    user_id = message.from_user.id
    data = message.text
    command, bot_token = data.split(" ")
    if  await db.is_bot_exist(bot_token):
        await msg.edit("This Bot Is aldready Running")
    else:
        try:
            clone_bot = Client(
                   f"{bot_token}", API_ID, API_HASH,
                   bot_token=bot_token,
                   plugins={"root": "clone_plugins"},
            )
            await clone_bot.start()
            bot = await clone_bot.get_me()
            bot_id = bot.id
            name = bot.first_name
            username = bot.username
            token = bot_token
            owner = user_id
            await db.add_bot(bot_id, name, username, token, owner)
            await msg.edit_text(f"✅ The bot @{bot.username} is now working like Groups Guard.\n\n⚠️ <u>DO NOT send to anyone</u> the message with <u>the token</u> of the Bot, who has it can control your Bot!\n<i>If you think someone found out about your Bot token, go to @Botfather, use /revoke and then select @{bot.username}</i>")
        except BaseException as e:
            await msg.edit_text(f"⚠️ <b>BOT ERROR:</b>\n\n<code>{e}</code>\n\n❔ Forward this message to @Master_broi to be fixed.")

        
                         
        
