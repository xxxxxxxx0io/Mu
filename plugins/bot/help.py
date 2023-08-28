# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 



from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules.strings import get_string, helpers
from modules import app
from modules.misc import SUDOERS
from modules.utils import help_pannel
from modules.utils.database import get_lang, is_commanddelete_on
from modules.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from modules.utils.inline.help import (help_back_markup,
                                          private_help_panel)




@app.on_message(
    filters.command(["help"])
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        if update.message.photo:
            await update.message.delete()
            await update.message.reply_text(
                "**●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●\n\n✧ ¦ مــرحـبآ بـگ يـﮯـآ عـسـل 😊 \n✧ ¦ آولآ گدهہ‏‏ آنآ بشـغل آغآنيـﮯ و فيـﮯديـﮯوهہ‏‏آت فيـﮯ آلگول 🎸\n✧ ¦ بـنزل آغآنيـﮯ و فيـﮯديـﮯوهہ‏‏آت بردو يـﮯســگر 📥\n✧ ¦ مـمـگن آشـتغل ف آلقنوآت و آلمــجمـوعآت 📢\n✧ ¦ فيـﮯ مـيـﮯزآت تآنيـﮯهہ‏‏ آضـآفيـﮯهہ‏‏ آگتشـفهہ‏‏آ بنفسـگ يـﮯآ قمـر 🌚\n✧ ¦ آضـغـطـ عليـﮯ زر **آوآمــر آلبـوت** \n✧ ¦ قـنآ‏‏هہ تحـديـﮯثآت آلـبوت [✮𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧✮](http://t.me/UIU_II)\n\n●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●", reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                "**●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●\n\n✧ ¦ مــرحـبآ بـگ يـﮯـآ عـسـل 😊 \n✧ ¦ آولآ گدهہ‏‏ آنآ بشـغل آغآنيـﮯ و فيـﮯديـﮯوهہ‏‏آت فيـﮯ آلگول 🎸\n✧ ¦ بـنزل آغآنيـﮯ و فيـﮯديـﮯوهہ‏‏آت بردو يـﮯســگر 📥\n✧ ¦ مـمـگن آشـتغل ف آلقنوآت و آلمــجمـوعآت 📢\n✧ ¦ فيـﮯ مـيـﮯزآت تآنيـﮯهہ‏‏ آضـآفيـﮯهہ‏‏ آگتشـفهہ‏‏آ بنفسـگ يـﮯآ قمـر 🌚\n✧ ¦ آضـغـطـ عليـﮯ زر **آوآمــر آلبـوت** \n✧ ¦ قـنآ‏‏هہ تحـديـﮯثآت آلـبوت [✮𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧✮](http://t.me/UIU_II)\n\n●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●", reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_text("**●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●\n\n✧ ¦ مــرحـبآ بـگ يـﮯـآ عـسـل 😊 \n✧ ¦ آولآ گدهہ‏‏ آنآ بشـغل آغآنيـﮯ و فيـﮯديـﮯوهہ‏‏آت فيـﮯ آلگول 🎸\n✧ ¦ بـنزل آغآنيـﮯ و فيـﮯديـﮯوهہ‏‏آت بردو يـﮯســگر 📥\n✧ ¦ مـمـگن آشـتغل ف آلقنوآت و آلمــجمـوعآت 📢\n✧ ¦ فيـﮯ مـيـﮯزآت تآنيـﮯهہ‏‏ آضـآفيـﮯهہ‏‏ آگتشـفهہ‏‏آ بنفسـگ يـﮯآ قمـر 🌚\n✧ ¦ آضـغـطـ عليـﮯ زر **آوآمــر آلبـوت** \n✧ ¦ قـنآ‏‏هہ تحـديـﮯثآت آلـبوت [✮𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧✮](http://t.me/UIU_II)\n\n●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●", reply_markup=keyboard)


@app.on_message(
    filters.command(["help"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        "**🥀 توآصـل بف » \nلمـعرفهہ‏‏ جمـيـﮯع آوآمـر آلبوت 💞 ...**", reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb5":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "🥀 آلآمـر للمـطـوريـﮯن 💞", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_5, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )



# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

