# Найти НОК двух чисел

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print('НОК = ', i)

