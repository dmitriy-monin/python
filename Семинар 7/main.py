import num as comp
import rat as rat
import logger as log

x = ""
y = ""
znak = ""

def get_numbers():
    global x
    global y
    global znak
    x = input('Введите первое число: ')
    y = input('Введите второе число: ')
    znak = input('Введите знак арифметической операции: ')
    data = x, y, znak
    return data



answer = input('Введите "y" если будем считать рациональные числа или "n" - если комплексные: ')
if answer == 'y':
    result = rat.calculator_rational(get_numbers())
    print(f'{x} {znak} {y} = {result}')

elif answer == 'n':
    result = comp.num(get_numbers())
    print(f'{x} {znak} {y} = {result}')

else: print('Только "y" или "n"')

log.log_add(x, y, znak, result)