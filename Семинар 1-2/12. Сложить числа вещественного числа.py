# Сложить числа вещественного числа

# 1 вариант
num = 424.7342
sum = 0

while num % 1 != 0:
    num = num*10
num=int(num)
num = str(num)

for i in num:
    i = int(i)
    sum = sum + i
    print(sum)

print(f'Сумма чисел: {sum}')

# 2 вариант
num = input('Введите число: ')
sum = 0

for i in num:
    if i != '.':
        sum += int(i)

print(f'Сумма чисел: {sum}')