# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from modules import app
from modules import config
from modules.config import BANNED_USERS
from modules.config.config import OWNER_ID
from modules.utils.helpers.filters import command
from modules.strings import get_command, get_string
from modules import Telegram, YouTube, app
from modules.misc import SUDOERS
from plugins.play.playlist import del_plist_msg
from plugins.sudo.sudoers import sudoers_list
from modules.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from modules.utils.decorators.language import LanguageStart
from modules.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(["start"])
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(
                _["help_1"], reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "🔎 Fetching your personal stats.!"
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[Telegram Files and Audios](https://t.me/telegram) ** played {count} times**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} has just started Og Music Bot to check <code>SUDOLIST</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "Failed to get lyrics."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**Video Track Information**__

❇️**Title:** {title}

⏳**Duration:** {duration} Mins
👀**Views:** `{views}`
⏰**Published Time:** {published}
🎥**Channel Name:** {channel}
📎**Channel Link:** [Visit From Here]({channellink})
🔗**Video Link:** [Link]({link})

⚡️ __Searched Powered By {config.MUSIC_BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch ", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🔄 Close", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} has just started Og Music Bot to check <code>VIDEO INFORMATION</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""**●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●\n\n✧ ¦ مـرحـبا بـك يـا عـسل 😊 \n✧ ¦ اولا كده انا بشغل اغاني و فيديوهات في الكول 🎸\n✧ ¦ بـنزل اغاني و فيديوهات بردو يسـكر 📥\n✧ ¦ ممكن اشتغل ف القنوات و المـجموعات 📢\n✧ ¦ في ميزات تانيه اضافيه اكتشفها بنفسك يا قمر 🌚\n✧ ¦ اضغـط علي زر **اوامـر البـوت** \n✧ ¦ قـناة تحـديثات الـبوت [✮𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧✮](http://t.me/UIU_II)\n\n●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ آضـفنيـﮯ آليـﮯ مـجمـوعتگ ❱ ➕", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙ ❰ اوامـر البـوت ❱ ⚙", callback_data="settings_back_helper")
                ]
           ]
        ),
                  )
            except:
                await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""**●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●\n\n✧ ¦ مـرحـبا بـك يـا عـسل 😊 \n✧ ¦ اولا كده انا بشغل اغاني و فيديوهات في الكول 🎸\n✧ ¦ بـنزل اغاني و فيديوهات بردو يسـكر 📥\n✧ ¦ ممكن اشتغل ف القنوات و المـجموعات 📢\n✧ ¦ في ميزات تانيه اضافيه اكتشفها بنفسك يا قمر 🌚\n✧ ¦ اضغـط علي زر **اوامـر البـوت** \n✧ ¦ قـناة تحـديثات الـبوت [✮𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧✮](http://t.me/UIU_II)\n\n●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ آضـفنيـﮯ آليـﮯ مـجمـوعتگ ❱ ➕", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙ ❰ اوامـر البـوت ❱ ⚙", callback_data="settings_back_helper")
                ]
           ]
        ),
              )
        else:
            await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""**●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●\n\n✧ ¦ مـرحـبا بـك يـا عـسل 😊 \n✧ ¦ اولا كده انا بشغل اغاني و فيديوهات في الكول 🎸\n✧ ¦ بـنزل اغاني و فيديوهات بردو يسـكر 📥\n✧ ¦ ممكن اشتغل ف القنوات و المـجموعات 📢\n✧ ¦ في ميزات تانيه اضافيه اكتشفها بنفسك يا قمر 🌚\n✧ ¦ اضغـط علي زر **اوامـر البـوت** \n✧ ¦ قـناة تحـديثات الـبوت [✮𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧✮](http://t.me/UIU_II)\n\n●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ آضـفنيـﮯ آليـﮯ مـجمـوعتگ ❱ ➕", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙ ❰ اوامـر البـوت ❱ ⚙", callback_data="settings_back_helper")
                ]
           ]
        ),
           )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} has just started Bgt Music Bot.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
            )


@app.on_message(
    command(get_command("START_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        "**✅ شكرًا لاستضافتي في {0}. \ n {1} ما زال حيًا.  \n\ n للحصول على أي مساعدة أو مساعدة ، تحقق من مجموعة الدعم والقناة.**".format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**Private Music Bot**\n\nOnly for authorized chats from the owner. Ask my owner to allow your chat first."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return



# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
