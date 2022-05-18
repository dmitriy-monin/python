# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

dict = []
n = int(input('ВВедите переменную N: '))
a = 1

for i in range(-n , n + 1):
    dict.append(i)

data = open('file.txt', 'r')

for i in data:
    index = int(i)
    a *= dict[index]

data.close()
print(a)
print(dict)