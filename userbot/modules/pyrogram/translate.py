# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from deep_translator import GoogleTranslator
from pyrogram.types import Message

from ... import app, gen

app.CMD_HELP.update(
    {
        "translate": (
            "translate",
            {
                "tr [ language code ] [ text ] | [ reply to message ]": "Translates The Message In Your Language.\n\nNote : Use Correct Language Codes To Translate In Your Language.",
                "trlist": "Get list of supported translating languages.",
            },
        )
    }
)


gtl = GoogleTranslator()


@app.on_message(gen(["tr", "tl", "translate"], allow=["sudo", "channel"]))
async def translate_handler(_, m: Message):
    reply = m.reply_to_message
    cmd = m.command

    try:
        lang = cmd[1] if app.long(m) > 1 else "id"

        await app.send_edit(m, f"**Translating in** `{lang}` . . .")

        languages = list((gtl.get_supported_languages(as_dict=True)).values())

        if not lang in languages:
            return await app.send_edit(
                m,
                "Bot doesn't support this language code, please try different one.",
                text_type=["mono"],
                delme=5,
            )

        if reply and reply.text:
            tdata = await translate(m, lang=lang, text=reply.text)
            await app.send_edit(m, f"**Translated to:** `{lang}`\n\n**Text:**`{tdata}`")

        elif not reply and len(m.text) <= 4096:
            if app.long(m) <= 2:
                return await app.send_edit(
                    m,
                    "Give me the language code with text.",
                    text_type=["mono"],
                    delme=3,
                )
            text = m.text.split(None, 2)[2]
            tdata = await translate(m, lang=lang, text=text)
            await app.send_edit(
                m, f"**Translated to:** `{lang}`\n\n**Text:** `{tdata}`"
            )
        else:
            await app.send_edit(
                m,
                "Something went wrong, please try again later !",
                text_type=["mono"],
                delme=5,
            )
    except Exception as e:
        await app.error(m, e)


async def translate(m: Message, lang, text):
    tr = GoogleTranslator(source="auto", target=lang)
    return tr.translate(text)


@app.on_message(gen(["trlist", "tllist", "translatelist"], allow=["sudo", "channel"]))
async def translatelang_handler(_, m):
    data = []
    data.clear()

    langs_list = gtl.get_supported_languages(
        as_dict=True
    )  # output: {arabic: ar, french: fr, english: en etc...}
    for keys, values in zip(langs_list.values(), langs_list.keys()):
        data.append(f"`{keys}` : `{values}`")

    await app.send_edit(m, "**Total languages:**\n\n" + "\n".join(data))
