from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import datetime
from spy import log
from Operation_real import calc
#from Operation import calc


async def calc_command(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    #calc_input_msg_select_type(update, context)
    #get_type_telegramm(update, context)
    log(update, context)
    msg = update.message.text
    items = msg.split()
    result = calc(a=items[1], b=items[3], oper=items[2])

    await update.message.reply_text(f'сумма чисел {items[1]} {items[2]} {items[3]} = {result}')


async def calc_input_msg_select_type(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    await update.message.reply_text(f'input number type(r - real, c - complex): \n')


async def get_type_telegramm(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    msg = update.message.text
    if msg in ('r', 'c'):
        reply_msg = 'Продолжаем'
    else:
        reply_msg = 'Не правильный выбор - выхожу (r - real, c - complex)'
    await update.message.reply_text(reply_msg)


async def hi_command(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    await update.message.reply_text(f'menu:\n /hi\n/time\n/sum\n/help\n')


async def time_command(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes._bot_data) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'сумма чисел {items[1]}+{items[2]}={int(items[1])+int(items[2])}')
