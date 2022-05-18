# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

list = []
summ = 0
a = 0
n = int(input('Введите число n '))
for i in range(1, n + 1):
    a = (1 + 1/i)**i
    list.append(a)
for i in list:
    summ += i
print(summ)