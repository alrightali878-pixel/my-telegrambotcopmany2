from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔹 جایگزین با توکن بات خودت
TOKEN = "8491644288:AAHYD8DgMjMDZjwKJ_mlxqm07cUWqqde6rA"

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\nبات با موفقیت فعال شد."
    )

# ساخت برنامه بات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# اجرا
app.run_polling()
