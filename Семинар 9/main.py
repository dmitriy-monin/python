import settings
import telebot
import random

bot = telebot.TeleBot(settings.BOT_TOKEN)

candies = 0
candy1 = 0
candy2 = 0
cand = random.randint(3, 7)


@bot.message_handler(content_types=['text'])
def start(message):
    global candies, player1, player2, candy1, candy2
    if message.text == '/candy':
        bot.send_message(message.from_user.id,
                         'Здравствуйте! Вас приветствует игра "Забери все конфеты!" \n'
                         'Основные правила игры: \n'
                         'Нам будет дано некоторое количество конфет,'
                         f'за один ход мы можем взять не более {cand} конфет.'
                         'Выигрывает тот, кто заберет последнюю конфету. \n'
                         'Итак, начнём!')
        bot.send_message(message.from_user.id,
                         'Давайте познакомимся. Первый игрок, как к Вам можно обращаться?')
        bot.register_next_step_handler(message, name_player2)
    else:
        bot.send_message(message.from_user.id, 'Напиши /candy')


def name_player2(message):
    global candies, player1, player2, candy1, candy2
    player1 = message.text
    bot.send_message(message.from_user.id,
                     'Второй игрок, и Вы представьтесь, пожалуйста.')
    bot.register_next_step_handler(message, play1)


def play1(message):
    global candies, player1, player2, candy
    player2 = message.text
    candies = random.randint(25, 35)
    bot.send_message(message.from_user.id,
                     f'Конфет на столе {candies}\n' f'Можно взять до {cand} шт. Берёт {player1}.')
    bot.register_next_step_handler(message, get_candies1)


def get_candies1(message):
    global candies, player1, player2, candy1, candy2, cand
    candy1 = int(message.text)
    if candy1 <= cand and candy1 > 0:
        candies -= candy1
        if candies > 0:
            bot.send_message(message.from_user.id,
                             f'Конфет на столе {candies}\n' f'Можно взять не больше {cand} конфет. Берёт {player2}.')
            bot.register_next_step_handler(message, get_candies2)
        else:
            bot.send_message(message.from_user.id,
                             f'Выиграл {player1}! Поздравляю!')
    else:
        bot.send_message(message.from_user.id,
                         f'{player1}, можно взять не больше {cand} и не меньше 1 конфеты. Попробуйте еще раз.')
        bot.register_next_step_handler(message, get_candies1)


def get_candies2(message):
    global candies, player1, player2, candy1, candy2, cand
    candy2 = int(message.text)
    if candy2 <= cand and candy2 > 0:
        candies -= candy2
        if candies > 0:
            bot.send_message(message.from_user.id,
                             f'Конфет на столе {candies}\n' f'Можно взять не больше {cand} конфет. Берёт {player1}.')
            bot.register_next_step_handler(message, get_candies1)
        else:
            bot.send_message(message.from_user.id,
                             f'Выиграл {player2}! Поздравляю!')
    else:
        bot.send_message(message.from_user.id,
                         f'{player2}, можно взять не больше {cand} и не меньше 1 конфеты. Попробуйте еще раз.')
        bot.register_next_step_handler(message, get_candies2)


bot.polling(none_stop=True, interval=0)
