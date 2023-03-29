"""
Создайте функцию генератор чисел Фибоначчи
"""


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fib()
for i in range(20):
    print(next(fib_gen))
