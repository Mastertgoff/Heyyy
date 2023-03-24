from urllib import response
import openai
from pyrogram import Client, filters, enums
from info import ADMINS
import datetime
import pytz
import asyncio 

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
    replied = message.reply_to_message
    if not replied:
        try:
            query = message.text.split(" ", maxsplit=1)[1]
        except:
            return await message.reply_text("Give Me Anything Man I Will Gibe Answers...")
        m = await message.reply_text("👀")
    #Get lost
        response = ai_responses(query)
        await message.reply_text(response)
        await m.delete()
    else:
        
