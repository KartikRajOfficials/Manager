from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from BullyRobot import pbot as client


ANON = "https://te.legra.ph/file/380118372c4f02dc3fef6.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [𝗕𝗹𝗮𝗰𝗸 𝗦𝗼𝘃𝗲𝗿𝗲𝗶𝗴𝗻-🇮🇩](https://t.me/BlackSovereignRoBot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [@gtxPrime](tg://user?id=1165094443)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

*𝗕𝗹𝗮𝗰𝗸 𝗦𝗼𝘃𝗲𝗿𝗲𝗶𝗴𝗻 sᴏᴜʀᴄᴇ ɪs not ᴩᴜʙʟɪᴄ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=1165094443"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://telegra.ph/file/9b0455dae14d5639f936d.mp4")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
