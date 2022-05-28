from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("5565678844:AAHcLJFaRngdp-7pkMwjbb1AiSe-3CWdJyg").build()
from telebot import types

@app.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  buttonA = types.KeyboardButton('A')
  buttonB = types.KeyboardButton('B')
  buttonC = types.KeyboardButton('C')

  markup.row(buttonA, buttonB)
  markup.row(buttonC)

  app.send_message(message.chat.id, 'It works!', reply_markup=markup)
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("game", game_command))

print('server start')
app.run_polling()