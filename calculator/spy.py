from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import datetime


def log(update: Update, context: ContextTypes._bot_data) -> None:
    file = open('db.csv', 'a')
    file.write(
        f'{datetime.datetime.now().time()}, {update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()
