# Copyright (C) 2019 The Raphielscape Company LLC.
# RAM-UBOT MINTA
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime, REPO_NAME
from userbot.events import register

gesss = [
    "**Halo kang ๐ค**",
    "**Hadir kang** ๐",
    "**Hi, kang kemana sj?** ๐ค",
    "**Hadir kak** ๐",
    "**Hadir kang** ๐",
    "**Hadir kang maap telat** ๐ฅบ",
    "**Saya slalu ada buat kang๐ฅต**",
    "**Bang landak, Aku ange๐๐**",
    "**Jangan kemana mana lagi ya bang๐ฅฐ**",
    "**Pas banget kang, aku lagi kangen๐ฅบ**",
    "**Akhirnya kang on juga**๐",
    "**Mau pap dari aku ndak kang** ๐",
    "**Salam hormat buat king Oscar** ๐ค",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=1467490218, pattern=r"^gesss$")
async def _(Oscar):
    await Oscar.reply(random.choice(gesss))


@register(outgoing=True, pattern="^.ping$")
@register(incoming=True, from_users=1467490218, pattern=r"^\.cping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("๐ก")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**MEMEK!!**\n**KEKUATAN MEMEK** : `%sms`\n**DURASI MEMEK** : `{uptime}๐`" % (duration))


@register(outgoing=True, pattern="^Ping$")
@register(incoming=True, from_users=1467490218, pattern=r"^\.cpi$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("PONG!!")
    await asyncio.sleep(2)
    await pong.edit(f"{REPO_NAME}")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"{REPO_NAME}!!\n"
                    f"OWNER : {ALIVE_NAME}\n `%sms`\n"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...โจ`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "โง **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **โโโโโโโโโโโโโโโโโ**\n\n"
                   "โง **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "โง **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "โง **Signal:** "
                   f"`{result['ping']}` \n"
                   "โง **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"โง **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("PONG")
    await asyncio.sleep(1)
    await pong.edit("๐ฅต")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**Oแดกษดแดส : {ALIVE_NAME}**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "๐พ๐ค๐ข๐ข๐๐ฃ๐: `.ping` or `.pings`\
         \nโณ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n๐พ๐ค๐ข๐ข๐๐ฃ๐: `Speed`\
         \nโณ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n๐พ๐ค๐ข๐ข๐๐ฃ๐: `Pong`\
         \nโณ : Sama Seperti Perintah Ping."})
