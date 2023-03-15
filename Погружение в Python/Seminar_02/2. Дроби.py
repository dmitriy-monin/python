# 3. Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions
import math

one = input('Введите первую дробь: ').split('/')
two = input('Введите вторую дробь: ').split('/')

numerator1 = int(one[0])
denominator1 = int(one[1])
numerator2 = int(two[0])
denominator2 = int(two[1])

sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2
divisor = math.gcd(sum_numerator, sum_denominator)
if divisor:
    sum_numerator //= divisor
    sum_denominator //= divisor

mult_numerator = numerator1 * numerator2
mult_denominator = denominator1 * denominator2
divisor = math.gcd(mult_numerator, mult_denominator)
if divisor:
    mult_numerator //= divisor
    mult_denominator //= divisor

print(f'{sum_numerator}/{sum_denominator}')
print(f'{mult_numerator}/{mult_denominator}')
print(f'{fractions.Fraction(numerator1, denominator1) + fractions.Fraction(numerator2, denominator2)}')
print(f'{fractions.Fraction(numerator1, denominator1) * fractions.Fraction(numerator2, denominator2)}')
