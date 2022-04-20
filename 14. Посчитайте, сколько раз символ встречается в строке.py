# Посчитайте, сколько раз символ встречается в строке.

string = 'Hello World'
symbol = 'о'
sum = 0

for i in string:
    if i == symbol: sum += 1

print(f'Символ  "{symbol}"  встречается {sum} раз')