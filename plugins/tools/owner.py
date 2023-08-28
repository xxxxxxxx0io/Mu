from pyrogram import Client, filters

from modules import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("زين")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""🥀 اخــو جـــوڪ الصـغيـر @G_O_OZ 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 زيـــــــٌن اݪــتأࢪيخ 🚸 🥀", url=f"https://t.me/p_m_4")
                ]
            ]
        ),
    )
