# Составить список простых множителей натурального числа N

n = int(input('Введите число: '))
n2 = []
while n!=1:
    if n%2==0:
        n=n//2
        n2.append(2)
    elif n%3==0:
        n=n//3
        n2.append(3)
    elif n%5==0:
        n=n//5
        n2.append(5)
    elif n%7==0:
        n=n//7
        n2.append(7)
    else:
        n2.append(n)
        n=1
print(n2)