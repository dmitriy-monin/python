def num(data):
    x, y, action = data
    a = complex(x)
    b = complex(y)
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b
    else:
        print('Ошибка ввода данных')
