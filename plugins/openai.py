from urllib import response
import openai
from pyrogram import Client, filters, enums
from info import ADMINS
import datetime
import pytz

OPEN_AI_KEY = "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"

def ai_responses(input_text):
    user_message = str(input_text).lower()
    prompt_addition = "ENTER YOUR PROMPT HERE" + user_message
    openai.api_key = OPEN_AI_KEY
    bot_output = openai.Completion.create(engine="text-davinci-002",prompt=prompt_addition,temperature=0.7,max_tokens=200,top_p=1,frequency_penalty=0,presence_penalty=0)
    response = bot_output['choices'][0]['text']
    return response
  
@Client.on_message(filters.command("openai") & filters.user(ADMINS))
async def delvarrrssz(bot, message):
    query = message.text.split(" ", maxsplit=1)[1]

    response = ai_responses(query)
    await message.reply_text(response)
    
@Client.on_message(filters.command("get") & filters.user(ADMINS))
async def delvarrrssz(bot, message):
    #Nothong Is Why...
    time = strftime("%H:")
    if time < 12:
        get="Good Morning"
    elif time < 15: 
        get="Good After Noon"
    else:
        get="Good Even"
    await message.reply_text(f"{get}")
