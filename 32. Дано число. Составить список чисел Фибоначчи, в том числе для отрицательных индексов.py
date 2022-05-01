# Дано число. Составить список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: 
# [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи


def fibo(n):
    if n>=0:
       idx = range(n+1)
       x = [0,1]
       for k in idx[2:]:
           x.append(x[k-1] + x[k-2]) 
       return x[n]
    else:
       n=-(n-1)
       idx = range(n+1)
       x = [1,0]
       for k in idx[2:]:
           x.append(x[k-2] - x[k-1]) 
       x.reverse()
    return x[0]

list = []
k = int(input('Введите число: '))
for i in range(-k,k+1):
   list.append(fibo(i))
print(list)