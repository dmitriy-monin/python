# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# 1 вариант
list = []
n =int(input('Введите число n '))
list.append(1)
for i in range(1, n):
    list.append(list[i-1]*(i+1))
print(list)

# 2 вариант
list = []
a = 1
n = int(input('Введите число n '))
for i in range(1, n + 1):
    a *= i
    list.append(a)
print(list)