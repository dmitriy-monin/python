# Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды 

num = int(input('Введите количество секунд: '))

day = 0
hour = 0
minute = 0
sec = 0

while num >= 86400:
    day += 1
    num -= 86400

while num >= 3600:
    hour += 1
    num -= 3600

while num >= 60:
    minute += 1
    num -= 60

sec = num

print(f'{day} дней {hour} часов {minute} минут {sec} секунд')