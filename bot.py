import os
import time
import asyncio
import pyrogram
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

OWNER = os.environ.get("OWNER", "")

Deccan = Client(
    "Country Info Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """
Hello {}, 

I am a **Country Information Finder** bot.

I can Get Information about any country.
"""
HELP_TEXT = """
Follow these steps..

☛ Just send me a country name..

☛ Then I will collect information & send to you..
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Deccan_Supportz')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Deccan_Supportz')
        ]]
    )

ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Deccan_Supportz')
        ]]
    )

@Deccan.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )

@Deccan.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
   country = CountryInfo(update.text)
   info = f"""
**Name** : `{country.name()}`
**Native Name** : `{country.native_name()}`
**Capital** : `{country.capital()}`
**Population** : `{country.population()}`
**Area[in km²]** : `{country.area()}`
**Region** : `{country.region()}`
**Sub Region** : `{country.subregion()}`
**Borders** : `{country.borders()}`
**Top Level Domains** : `{country.tld()}`
**Calling Codes** : `{country.calling_codes()}`
**Currencies** : `{country.currencies()}`
**Residence** : `{country.demonym()}`
**Timezone** : `{country.timezones()}` 
"""
   country_name = country.name()
   country_name = country_name.replace(" ", "+")
   reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country_name}'),
        InlineKeyboardButton('Yahoo', url=f'https://www.yahoo.com/search?q={country_name}')
        ]]
   try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
   except FloodWait as floodwait:
        await asyncio.sleep(floodwait.x)
        return countryinfo(bot, update)
   except KeyError as keyerror:
        print(keyerror)
   except Exception as error:
        print(error)
   

Deccan.run()
