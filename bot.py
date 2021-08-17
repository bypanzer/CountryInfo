import os
import time
import asyncio
import pyrogram
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

OWNER = os.environ.get("OWNER", "1518238620")

Deccan = Client(
    "Country Info Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """
Salam {}, 

Mən **Coğrafiyaçı'm** botam.

Mən istənilən ölkə haqqında məlumat əldə edə bilirəm.
"""
HELP_TEXT = """
Bu addımları izlə..

☛ İndi mənə istədiyin ölkə adını göndər..

☛ Mən məlumat toplayıb sənə göndərəcəm🙆..
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Creator 🙇', url='https://t.me/hasanli517')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Creator 🙇', url='https://t.me/hasanıi517')
        ]]
    )

ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Creator 🙇', url='https://t.me/hasanli517')
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
**Ölkə adı(Qlobal)** : `{country.name()}`
**Ölkə adı(Yerli)** : `{country.native_name()}`
**Paytaxt** : `{country.capital()}`
**Əhali** : `{country.population()}`
**Ərazi[km² ilə]** : `{country.area()}`
**Region** : `{country.region()}`
**Sub Region** : `{country.subregion()}`
**Sərhədlər** : `{country.borders()}`
**Ölkə domeni** : `{country.tld()}`
**Beynəlxalq Zəng Kodu** : `{country.calling_codes()}`
**Məzənnə** : `{country.currencies()}`
**Milliyyət** : `{country.demonym()}`
**Saat qurşağı** : `{country.timezones()}` 
"""
   country_name = country.name()
   country_name = country_name.replace(" ", "+")
   reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country_name}'),
        InlineKeyboardButton('Yahoo', url=f'https://www.yahoo.com/search?q={country_name}')
        ]]
     ) 
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
