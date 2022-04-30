# Определить, присутствует ли в заданном списке строк, некоторое число

list = ['a , 2 , 4' 
        't , 6 , 2'
        'f , 1 , 3']
n = 1
f = False
for i in range(len(list)):
    for a in list[i]:
        if a == str(n):
            f = True
            break

print(f)