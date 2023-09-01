# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import Client, filters

from modules import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("سورس")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""🥀 [ωєℓcσмє τσ sσυяcє zє🎸](https://t.me/UI_XB)\n\n[✘ ժᥱ᥎ ๓๑ᴆỿ ✘ 🎸](https://t.me/UP_UO)\n\n[✘ ժᥱ᥎ Ꭹ๑Ꭹ๑  ✘🎸](https://t.me/FC_SI)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 sσυяcє sєzαя 🥀", url=f"https://t.me/UI_XB")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮 🥀", url=f"https://t.me/UP_UO")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𐇮 𝑴𝑹𝑨𝑻 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮 🥀", url=f"https://t.me/FC_SI"
                    ),
                    InlineKeyboardButton(
                        "🥀 جروب آلدعمـ 🥀", url=f"https://t.me/UI_OS")
                ]
            ]
        ),
    ) 

# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
