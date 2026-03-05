import os
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, SESSION, CHANNEL

app = Client("MusicBot", API_ID, API_HASH, bot_token=BOT_TOKEN)
assistant = Client("Assistant", API_ID, API_HASH, session_string=SESSION)
call_py = PyTgCalls(assistant)

@app.on_message(filters.command("شغل", prefixes=""))
async def play(client, message):
    # تحقق الاشتراك الإجباري
    if CHANNEL:
        try:
            await client.get_chat_member(CHANNEL, message.from_user.id)
        except UserNotParticipant:
            return await message.reply(f"❌ عذراً، اشترك بالقناة أولاً:\n@{CHANNEL}")
        except: pass
    
    if len(message.command) < 2:
        return await message.reply("⚡️ أرسل: شغل + اسم الأغنية")
    await message.reply("⏳ جاري البحث والتحضير...")

@app.on_message(filters.command("انهاء", prefixes=""))
async def stop(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply("🛑 تم إيقاف التشغيل.")
    except: pass

print("✅ السورس يعمل بنجاح...")
call_py.start()
app.run()
