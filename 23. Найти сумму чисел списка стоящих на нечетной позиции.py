# Найти сумму чисел списка стоящих на нечетной позиции

from random import randint

list = []
sum = 0

for i in range(randint(1, 15)):
    list.append(randint(10, 30))

for i in range(0, len(list), 2):
    sum += list[i]

print(list)
print(sum)