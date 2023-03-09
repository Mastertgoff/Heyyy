from pyrogram import Client 
import heroku3
from info import ADMINS

HRK_API = "3650d48d-2d02-49f8-b406-2d8a3a840af4"
HRK_APP_NAME = "calm-scrubland-89456"

heroku_conn = heroku3.from_key('HRK_API')
                               
app = heroku_conn.app(HRK_APP_NAME)

@Client.on_message(filters.command("setvar") & filters.user(ADMINS))
async def setvarrrz(bot, message):
    data = message.text        
    command, varname, value = data.split(" ")
    config = app.config()
    config[f'{varname}'] = f'{value}'
