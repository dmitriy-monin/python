from fractions import Fraction


def calculator_rational(data):
  a, b, c = data
  a = Fraction(a)
  b = Fraction(b)
  if c == '+':
    return a + b
  if c == '-':
    return a - b
  if c == '*':
    return a * b
  if c == '/':
    return a / b
  else:
    print('Ошибка ввода данных')