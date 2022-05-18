# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

a = []
n = 1
count = int(input('Введите число: '))

for i in range(count):
    a.append(n)
    n *= -3
print(a)