# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Я загадал число от 0 до 1000. Попробуй угадать его за 10 попыток!')
for i in range(0, ATTEMPTS):
    while True:
        search = input(f'Осталось попыток {ATTEMPTS - i}. Введи число: ')
        if search.isdigit():
            search = int(search)
            break
        print('Кажется это не число. Попробуй еще раз!')
    if i == ATTEMPTS - 1:
        print('К сожалению ты не угадал загаданное число!')
    elif num > search and i < ATTEMPTS:
        print('Попробуй ввести число БОЛЬШЕ!')
    elif num < search and i < ATTEMPTS:
        print('Попробуй ввести число МЕНЬШЕ!')
    else:
        print(f'Ура! Ты угадал! Я загадывал число {num}!')
        break
