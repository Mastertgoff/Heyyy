from pyrogram import Client, filters
from pyrogram.types import Message
from info import ADMINS

@Client.on_message(filters.user(ADMINS) & filters.command("start"))
async def eval(client, message):
    status_message = await message.reply_text("clone starting ")
