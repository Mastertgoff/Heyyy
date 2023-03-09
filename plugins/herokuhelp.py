from pyrogram import Client 
import heroku3
from info import ADMINS

HRK_API = 
HRK_APP_NAME = 

heroku_conn = heroku3.from_key('HRK_API)
                               
app = heroku_conn.apps()['HRK_APP_NAME']

@Client.on_message(filters.command("setvar") & filters.user(ADMINS))
async def setvarrrz(bot, message):
    data = message.text        
    command, varname, value = data.split(" ")
    config = app.config()
    config[f'{varname}'] = f'{value}'
                   
