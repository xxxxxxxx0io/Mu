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
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""🥀 [ωєℓcσмє τσ sσυяcє sєzαя︎🎸](https://t.me/UIU_II)\n\n[✘ ժᥱ᥎ zєiи ✘ 🎸](https://t.me/p_m_4)\n\n[✘ ժᥱ᥎ jσĸ  ✘🎸](https://t.me/G_O_OZ)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 sσυяcє sєzαя 🥀", url=f"https://t.me/UIU_II")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 زيـــــــٌن اݪــتأࢪيخ 🚸 🥀", url=f"https://t.me/p_m_4")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 ⧛ َ𝗝َ َ𝗢َ ٍ𝗞َ ׀ مــ ـٰٖمـوِٰلٰ ׀ جـِوڪَ ׀ ⧚ 🥀", url=f"https://t.me/G_O_OZ"
                    ),
                    InlineKeyboardButton(
                        "🥀 جروب آلدعمـ 🥀", url=f"https://t.me/SORS0C")
                ]
            ]
        ),
    ) 

# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 