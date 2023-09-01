from pyrogram import Client, filters

from modules import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("مودي")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""🥀 MODY,Social Media Sponsored,Bot Developer With More Than One Users: @UI_XB @UI_OS @UI3I3 insta:( http://www.instagram.com/wfj.x) 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮 🥀", url=f"https://t.me/UP_UO")
                ]
            ]
        ),
    )
