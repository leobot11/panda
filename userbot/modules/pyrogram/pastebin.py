# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import asyncio

from pyrogram.types import Message

from ... import app, gen


app.CMD_HELP.update(
    {
        "nekobin": (
            "nekobin",
            {
                "bin [reply to text]": "Paste Texts To Nekobin Site, You Can Easily Read The Texts Without Downloading The file."
            },
        )
    }
)


@app.on_message(gen(["paste", "bin"], allow=["sudo"]))
async def paster_handler(_, m: Message):
    reply = m.reply_to_message

    if reply and reply.text or reply.caption:
        text = reply.text or reply.caption
    elif not reply and app.long(m) > 1:
        text = m.text.split(None, 1)[1]
    elif not reply and app.long(m) == 1:
        return await app.send_edit(
            m,
            "Please reply to a message or give some text after command.",
            text_type=["mono"],
            delme=4,
        )

    m = await app.send_edit(m, "Pasting to pastebin . . .", text_type=["mono"])
    url = await app.HasteBinPaste(text)
    reply_text = f"**Hastebin** : [Click Here]({url})"
    delete = (
        True
        if app.long(m) > 1 and m.command[1] in ["d", "del"] and reply.from_user.is_self
        else False
    )
    if delete:
        await asyncio.gather(
            app.send_edit(m, reply_text, disable_web_page_preview=True),
            await reply.delete(),
        )
    else:
        await app.send_edit(m, reply_text, disable_web_page_preview=True)
