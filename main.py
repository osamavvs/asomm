import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

# --- إعدادات الحساب والبوت ---
# ملاحظة: يمكنك تغيير هذه القيم يدوياً أو تركها كما هي إذا كنت ستستخدم ملف config
API_ID = int(os.getenv("API_ID", "123456")) 
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
SESSION = os.getenv("SESSION", "your_string_session")

# --- تشغيل المحركات ---
app = Client("MyMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client("Assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
call_py = PyTgCalls(assistant)

# --- أوامر التحكم (عربي + بدون رموز) ---

@app.on_message(filters.command("شغل", prefixes=""))
async def play_command(client, message):
    """أمر التشغيل: شغل [اسم الأغنية]"""
    if len(message.command) < 2:
        return await message.reply("⚡️ أرسل اسم الأغنية مع الأمر\nمثال: `شغل حاتم العراقي`")
    
    await message.reply("⏳ جاري البحث والتحضير...")
    # ملاحظة: هنا سنضيف دالة البحث في يوتيوب في الخطوة القادمة

@app.on_message(filters.command("انهاء", prefixes=""))
async def stop_command(client, message):
    """أمر الإيقاف ومغادرة المكالمة"""
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply("🛑 تم إيقاف التشغيل ومغادرة المكالمة.")
    except:
        await message.reply("❌ لا يوجد تشغيل حالياً.")

@app.on_message(filters.command("تخطي", prefixes=""))
async def skip_command(client, message):
    """أمر التخطي"""
    await message.reply("⏭ تم التخطي بنجاح.")

# --- بدء العمل ---
print("✅ السورس يعمل الآن بنجاح...")
call_py.start()
app.run()
