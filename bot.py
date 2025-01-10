from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai

# OpenAI API sozlamalari
openai.api_key = "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"

# Salomga alik olish funksiyasi
async def greet(update: Update, context):
    user_message = update.message.text.lower()
    if "salom" in user_message:
        await update.message.reply_text("Salom! Qalaysiz?")
    else:
        await update.message.reply_text('Meni "salom" deb chaqirishingiz mumkin.')

# Sun'iy intellekt bilan muloqot qilish funksiyasi
async def ai_chat(update: Update, context):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_reply = response.choices[0].message.content
        await update.message.reply_text(ai_reply)
    except Exception as e:
        await update.message.reply_text("Kechirasiz, biror xatolik yuz berdi. Keyinroq urinib ko'ring.")
        print(f"Xatolik: {e}")

# /start komandasi uchun funksiya
async def start_command(update: Update, context):
    await update.message.reply_text(
        "Assalomu alaykum! Men sun'iy intellektga asoslangan Telegram botman. "
        "Menga "salom" deb murojaat qilsangiz yoki boshqa savollaringiz bo'lsa, bemalol yozing!"
    )

# Botni sozlash va boshlash
if __name__ == "__main__":
    app = ApplicationBuilder().token("6324913233:AAFd0K0wv4Rz0ClIoJf0VOGnOGyxY7oUZBI").build()

    # Handlers qo'shish
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, greet))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat))

    print("Bot ishga tushdi!")
    app.run_polling()
