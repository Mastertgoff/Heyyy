from pyrogram import Client, filters, enums
import heroku3
from info import ADMINS

HRK_API = "3650d48d-2d02-49f8-b406-2d8a3a840af4"
HRK_APP_NAME = "calm-scrubland-89456"

heroku_conn = heroku3.from_key(HRK_API)
#apps = heroku_conn.apps()[HRK_APP_NAME]                             
app = heroku_conn.app(HRK_APP_NAME)

@Client.on_message(filters.command("setvar") & filters.user(ADMINS))
async def setvarrrz(bot, message):
    ms = await message.reply_text(text="<b>Proccesing...</b>")
    data = message.text        
    command, varname, value = data.split(" ")
    config = app.config()
    if varname in config:
        await ms.edit(text=f"Updated {varname} In {value}")
        config[varname] = value
    else:
        #More
        await ms.edit(text=f"<b>Completed..\nAdded New Varible In Heroku..\n\nVar Name : {varname}\nValue : {value}</b>")
        config[varname] = value
    
@Client.on_message(filters.command("delvar") & filters.user(ADMINS))
async def delvarrrz(bot, message):
    ms = await message.reply_text(text="<b>Proccesing...</b>")
    data = message.text        
    command, varname = data.split(" ")
    config = app.config()
    if not in varname: 
        await ms.edit(text=f"{varname} Not Found")
    else:   
        await ms.edit(text=f"<code>Deleted A New Config Var {varname}✅️</code>")
        del config[varname]
