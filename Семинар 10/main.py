import wikipedia, settings, telebot

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/wiki':
        bot.send_message(message.from_user.id, 'Здравствуйте! Что будем искать?')
        bot.register_next_step_handler(message, answer)
    else:
        bot.send_message(message.from_user.id, 'Напиши /wiki')


def answer(message):
    wikipedia.set_lang("ru")
    answer = message.text
    answer = wikipedia.summary(answer)
    bot.send_message(message.from_user.id, answer)
    bot.send_message(message.from_user.id, 'Для следующего запроса напиши /wiki')


bot.polling(none_stop=True, interval=0)
