# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP, REPO_NAME, EMOJI_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(rambot):
    """ For .help command,"""
    args = rambot.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await rambot.edit(str(CMD_HELP[args]))
        else:
            await rambot.edit("**`NGETIK YANG BENER NAPA TOLOLLL!`**")
            await asyncio.sleep(50)
            await rambot.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t {EMOJI_HELP}  "
        await rambot.edit(f"**{REPO_NAME}**\n\n"
                         f"**{EMOJI_HELP} πΏπ΄πΌπΈπ»πΈπΊ π±πΎπ : {DEFAULTUSER}**\n**{EMOJI_HELP}  πΌπΎπ³ππ»π΄π : {len(modules)}**\n\n"
                         f"**{EMOJI_HELP} ππ΄πΌππ° πΌπ΄π½π :**\n\n βββββββββββ£β β ββ ββββββββββ\n\n"
                         f"{EMOJI_HELP} {string}\n\n βββββββββββ£β β ββ ββββββββββ\n\nNGETIK YANG BENER NAPA TOLOLLL!!\n\n")
        await rambot.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha..")
        await asyncio.sleep(50)
        await rambot.delete()
