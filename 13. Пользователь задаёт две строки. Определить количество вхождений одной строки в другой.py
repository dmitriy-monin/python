# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

one = 'hello'
two = 'hello world hello'

spl = two.split(' ')
count = 0

for i in range(len(spl)):
    if one == spl[i]:
        count += 1
print(count)