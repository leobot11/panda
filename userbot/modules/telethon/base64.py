import asyncio
import base64
from . import PandaBot, edit_or_reply


plugin_category = "plugins"




@PandaBot.ilhammansiz_cmd(
    pattern="en(?: |$)(.*)",
    command=("encode", plugin_category),
    info={
        "header": "encode ",
        "usage": "{tr}en text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Encode..`")
    byt = ppk.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await edit_or_reply(event,
        f"**=>> Encoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
    )

@PandaBot.ilhammansiz_cmd(
    pattern="de(?: |$)(.*)",
    command=("decode", plugin_category),
    info={
        "header": "decode ",
        "usage": "{tr}de text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Decode..`")
    byt = ppk.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await edit_or_reply(event,
            f"**=>> Decoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await edit_or_reply(event, "**ERROR :** " + str(p))






@PandaBot.ilhammansiz_cmd(
    pattern="enurl(?: |$)(.*)",
    command=("urlencode", plugin_category),
    info={
        "header": "url encode ",
        "usage": "{tr}en text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Encode..`")
    byt = ppk.encode("ascii")
    et = base64.urlsafe_b64encode(byt)
    atc = et.decode("ascii")
    await edit_or_reply(event,
        f"**=>> Encoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
    )

@PandaBot.ilhammansiz_cmd(
    pattern="urlde(?: |$)(.*)",
    command=("urldecode", plugin_category),
    info={
        "header": "urldecode ",
        "usage": "{tr}urlde text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Decode..`")
    byt = ppk
    try:
        et = base64.urlsafe_b64decode(byt)
        atc = et
        await edit_or_reply(event,
            f"**=>> Decoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await edit_or_reply(event, "**ERROR :** " + str(p))


_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}
import ipaddress
import struct

@PandaBot.ilhammansiz_cmd(
    pattern="destring(?: |$)(.*)",
    command=("destring", plugin_category),
    info={
        "header": "destring ",
        "usage": "{tr}destring string pyro",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if len(ppk) in _PYRO_FORM.keys():
        data_ = struct.unpack(
                _PYRO_FORM[len(ppk)],
                base64.urlsafe_b64decode(ppk + "=" * (-len(ppk) % 4)),
        )
        if len(ppk) in [351, 356]:
            auth_id = 2
        else:
            auth_id = 3

        dc_id, tesmode, auth_key = data_[0], data_[2], data_[auth_id]       
    try:
        et = dc_id, auth_key
        atc = et
        tes = tesmode
        await edit_or_reply(event,
            f"**=>> Decoded Text :** `{data_}`\n\n**=>> OUTPUT :**\n`{atc}`  mode> {tesmode} "
        )
    except Exception as p:
        await edit_or_reply(event, "**ERROR :** " + str(p))

