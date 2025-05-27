from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

grades = {
    "yazan": "78",
    "ahmad": "85",
    "sara": "92"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! أرسل اسمك لأعطيك علامتك.")

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.lower()
    if name in grades:
        await update.message.reply_text(f"علامتك هي: {grades[name]}")
    else:
        await update.message.reply_text("الاسم غير موجود.")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7416194437:AAG13IAV_Ddv0TM78GYQqddmWKXGyAOQ7MY").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    app.run_polling()
