# Напишите программу, которая выводит нечетные числа из заданного списка 
# и останавливается, если встречает число 554.

# 1 вариант
list = [2, 4, 3, 2, 76, 7, 77, 554, 88, 99, 1]

for i in list:
    if i % 2 != 0:
        print(i)
    if i == 554:
        break

# 2 вариант
number = 0
list = []

while number != 554:
    number = int(input('Введите число: '))
    if number %2 != 0: list.append(number)
print(list)