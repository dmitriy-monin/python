# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.

data = 'aaaabbbcddddaaaac'
final = ''
count = 1
start = ''
for i in data:
    if i != start:
        if start != '':
            final +=str(count) + start
        count =1
        start = i
    else:
        count+=1
final +=str(count) + data[-1]
print(final)