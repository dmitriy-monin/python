from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from log import *

async def hi_command(update: Update, context: ContextTypes.context):
    logging(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.context):
    logging(update, context)
    await update.message.reply_text(f'/hi - Приветствие\n/time - Текущее время\n/sum - Сумма двух чисел\n/help - Справка')

async def time_command(update: Update, context: ContextTypes.context):
    logging(update, context)
    await update.message.reply_text(f'Текущее время: {datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.context):
    logging(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')