from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
from bot_command import *


async def hello(update: Update, context: ContextTypes._bot_data) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(
    "5965147034:AAEhjg9qCzANwBlPU7YkFGp_9Ep-_3eAihI").build()
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("sum", sum_command))
print('server start')
app.run_polling()
