from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 OTC Vision AI\n\n"
        "البوت يعمل الآن.\n"
        "استخدم /analysis أو /stats"
    )


async def analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 لا توجد تحليلات متاحة حالياً."
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 عدد التحليلات: 0\n"
        "نسبة النجاح التاريخية: --"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analysis", analysis))
app.add_handler(CommandHandler("stats", stats))

app.run_polling()
