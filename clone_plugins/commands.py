from pyrogram import Client, filters
from pyrogram.types import Message

@clone_bot.on_message(filters.user(ADMINS) & filters.command("start"))
async def eval(client, message):
    status_message = await message.reply_text("clone starting ")
