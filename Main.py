import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# إعداد صلاحيات Google Sheets API
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# تحميل بيانات الدخول من ملف key.json
CREDS = ServiceAccountCredentials.from_json_keyfile_name("key.json", SCOPE)
CLIENT = gspread.authorize(CREDS)

# افتح الشيت باسم ملف Google Sheets عندك (غيره)
SHEET = CLIENT.open("grades-bot").sheet1

# ضع توكن بوت التيليغرام هنا مباشرة
TOKEN = "7416194437:AAG13IAV_Ddv0TM78GYQqddmWKXGyAOQ7MY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! أرسل اسمك لأعطيك علامتك.")

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.lower()
    data = SHEET.get_all_records()

    for row in data:
        if row['name'].lower() == name:
            await update.message.reply_text(f"علامتك هي: {row['grade']}")
            return

    await update.message.reply_text("الاسم غير موجود.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    app.run_polling()
