from pyrogram import Client, filters, enums
from info import ADMINS, API_ID, API_HASH
import re
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
from database.clone_botsdb import save_bot_details

@Client.on_message(filters.command("clone") & filters.user(ADMINS))
async def delvarrrssz(bot, message):
    msg = await message.reply_text("Proccesing.. ")
    user_id = message.from_user.id
    data = message.text
    command, bot_token = data.split(" ")
    try:
        clone_bot = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "clone_plugins"},
        )
        await clone_bot.start()
        bot = await clone_bot.get_me()
        details = {
            'bot_id': bot.id,
            'is_bot': True,
            'user_id': user_id,
            'name': bot.first_name,
            'token': bot_token,
            'username': bot.username
        }
        save_bot_details(details)

        
        await msg.edit_text(f"✅ The bot @{bot.username} is now working like Groups Guard.\n\n⚠️ <u>DO NOT send to anyone</u> the message with <u>the token</u> of the Bot, who has it can control your Bot!\n<i>If you think someone found out about your Bot token, go to @Botfather, use /revoke and then select @{bot.username}</i>")
    except BaseException as e:
        await msg.edit_text(f"⚠️ <b>BOT ERROR:</b>\n\n<code>{e}</code>\n\n❔ Forward this message to @Master_broi to be fixed.")
