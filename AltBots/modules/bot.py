import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"𝐊𝙸𝙽𝙶 𝙸𝚂 Сσмιиɢ")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"𝐊ʏα 𝐎яᴅɛя 𝐇αι 𝐌ɛяɛ [𝐌αsтɛя](https://t.me/SAIF_DICTATOR)")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sstop(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"` Κιиɢ ϰ ៜραм ៜтσρɛƉ...`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"𝗔𝙳𝙳𝙸𝙽𝙶 𝚂𝚄𝙳𝙾 𝙱𝙾𝚂𝚂....__")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("𝙿𝙻𝙴𝙰𝚂𝙴 𝚃𝙰𝙶 𝚄𝚂𝙴𝚁 𝚃𝙾 𝙹𝙾𝙸𝙽 𝙰𝚁𝙼𝚈 !!")
            return

        if str(target) in sudousers:
            await ok.edit(" 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙺𝙸𝙽𝙶 𝚇 𝚂𝙿𝙰𝙼 𝚂𝙾𝙻𝙳𝙸𝙴𝚁")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `𝚂𝚄𝙳𝙾 𝙰𝙳𝙳 𝚂𝚄𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙺𝙸𝙽𝙶 𝙸𝚂 𝙲𝙾𝙼𝙸𝙽𝙶.....`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("ᴋʏᴀᴅᴇ ᴍᴇ ʀʜᴏ ғʏᴅᴇ ᴍᴇ ʀʜᴏɢᴇ ʙᴇᴡᴀᴋᴜғ ᴋʜɪᴋᴇ")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
async def rmsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)
        ok = await event.reply(f"Ɍεʍσʏιиɢ sʋƉʋ Ғяσм вɛωαғα ʋƨɛя...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:\nPlease set up your HEROKU_APP_NAME`")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇ ᴜsᴇʀ.")
            return
        if str(target) not in sudousers:
            await ok.edit("ᴜsᴇʀ ɪs ɴᴏᴛ ɪɴ ᴛʜᴇ sᴜᴅᴏ ʟɪsᴛ.")
        else:
            new_sudo_users = " ".join([user for user in sudousers.split() if user != str(target)])
            await ok.edit(f"ʙᴇᴡᴀғᴀ sᴜᴅᴏ ᴜsᴇʀ: `{target}`")
            heroku_var["SUDO_USERS"] = new_sudo_users
    else:
        await event.reply("ᴏɴʟʏ ᴋɪɴɢ ᴏᴡɴᴇʀ ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ.")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "🅣🅞🅣🅐🅛 🅢🅤🅓🅞 🅤🅢🅔🅡 🅞🅕 🅚🅘🅝🅖 :\n"
        for user_id in SUDO_USERS:
            sudo_users_list += f"- {user_id}\n"
        await event.reply(sudo_users_list)
    else:
        await event.reply("ᴘᴀᴅʜʟᴇ ᴊᴀ ᴋᴀʀ ɴᴀʟʟᴇ ʙʜᴀᴋᴀʀɪ .")
