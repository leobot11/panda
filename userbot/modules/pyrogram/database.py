from pyrogram.types import Message

from ... import app, gen

app.CMD_HELP.update(
    {
        "database": (
            "database",
            {
                "setdb [varname] [value]": "Set any database vars, for ex: .setdv [USER_NAME] [RYOISHIN]",
                "getdb [varname]": "Get a existing database vars value.",
                "deldb [varname]": "Delete a existing database var with its value.",
                "alldb": "Get all existing database vars.",
                "listdb": "Get all available dv vars which you set.",
            },
        )
    }
)


@app.on_message(gen("setdb", allow=["sudo"]))
async def setdv_handler(_, m: Message):
    if app.long(m) == 1:
        await app.send_edit(
            m, "Give me a key & a value to set dv vars.", text_type=["mono"], delme=4
        )

    elif app.textlen(m) > 4096:
        await app.send_edit(
            m,
            "Text is too long. only 4096 characters are allowed.",
            text_type=["mono"],
            delme=4,
        )

    elif app.long(m) == 2:
        await app.send_edit(
            m, "Please give me key with a value.", text_type=["mono"], delme=4
        )

    elif app.long(m) > 2:
        key = m.command[1]
        value = m.text.split(None, 2)[2]
        done = app.setdv(key, value)

        if done:
            await app.send_edit(
                m,
                f"Added database var with [ **key** = `{key}` ] and [ **value** = `{value}` ]",
            )

        elif not done:
            await app.send_edit(
                m,
                "Failed to a add key & value to database var.",
                text_type=["mono"],
                delme=2,
            )


@app.on_message(gen("deldb", allow=["sudo"]))
async def deldv_handler(_, m: Message):
    if app.long(m) == 1:
        await app.send_edit(
            m,
            "Give me some key to delete that a var from database . . . ",
            text_type=["mono"],
            delme=2,
        )

    elif app.textlen(m) > 4096:
        await app.send_edit(
            m,
            "text is too long. only 4096 characters are allowed.",
            text_type=["mono"],
            delme=4,
        )

    elif app.long(m) > 1:
        keys = "**Deleted vars:**\n\n"
        cmd = m.command
        for key in cmd[1:]:
            app.deldv(key)
            keys += f"`{key}`"

        await app.send_edit(m, f"Successfully deleted keys.\n\n{keys}", delme=4)
    else:
        await app.send_edit(
            m, "Something went wrong, try again later !", text_type=["mono"], delme=4
        )


@app.on_message(gen("getdb", allow=["sudo"]))
async def getdv_handler(_, m: Message):
    if app.long(m) == 1:
        await app.send_edit(
            m,
            "Give me some key to get value that a var from database . . . ",
            text_type=["mono"],
            delme=2,
        )

    elif app.long(m) > 1:
        key = m.command[1]
        done = app.getdv(key)

        if done:
            await app.send_edit(
                m, f"**Here:**\n\n**key** = `{key}`\n\n**value** = `{done}`", delme=4
            )
        else:
            await app.send_edit(
                m, "This var doesn't exist in my database.", text_type=["mono"], delme=4
            )
    else:
        await app.send_edit(
            m,
            "Maximum 4096 characters in one message . . .",
            text_type=["mono"],
            delme=4,
        )





@app.on_message(gen("alldb", allow=["sudo"]))
async def alldv_handler(_, m: Message):
    if app.getalldv() is True:
        m = await app.send_edit(
            m, "Getting all database vars . . .", text_type=["mono"]
        )
        my_dict = app.getalldv()
        dict_data = []
        dict_data.clear()

        for key, value in zip(my_dict.keys(), my_dict.values()):
            dict_data.append(f"`{key}` = `{value}`\n\n")

        await app.send_edit(m, "**All DB VARS:**\n\n" + "".join(dict_data))
    else:
        await app.send_edit(
            m, "There are no database vars (empty) !", text_type=["mono"], delme=4
        )


@app.on_message(gen("listdb", allow=["sudo"]))
async def dvlist_handler(_, m: Message):
    allvars = [f"`{x}`" for x in app.DVLIST]
    await app.send_edit(m, "**AVAILABLE DB VARS:**\n\n" + "\n".join(allvars))
