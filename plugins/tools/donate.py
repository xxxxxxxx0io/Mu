from pyrogram import Client, filters

from modules import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("جوك")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""🥀 JOKجـِوڪ,Social Media Sponsored,Bot Developer With More Than One Users: @JK_KI @JX_JK @fc_cq insta:( http://www.instagram.com/J_O_K_storm) 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 ⧛ َ𝗝َ َ𝗢َ ٍ𝗞َ ׀ مــ ـٰٖمـوِٰلٰ ׀ جـِوڪَ ׀ ⧚ 🥀", url=f"https://t.me/G_O_OZ")
                ]
            ]
        ),
    )
