# 2. Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_INDEX = 16
num = 123456789
new_num = ''
num1 = num

while num > 0:
    mid = num % HEX_INDEX
    match mid:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            new_num = str(mid) + new_num
        case 10:
            new_num = 'a' + new_num
        case 11:
            new_num = 'b' + new_num
        case 12:
            new_num = 'c' + new_num
        case 13:
            new_num = 'd' + new_num
        case 14:
            new_num = 'e' + new_num
        case 15:
            new_num = 'f' + new_num
    num = num // HEX_INDEX

match HEX_INDEX:
    case 2:
        print(str(num1) + ' in binary = ' + bin(num1))
        new_num = str(num1) + ' in binary = 0b' + new_num
    case 8:
        print(str(num1) + ' in oct = ' + oct(num1))
        new_num = str(num1) + ' in oct = 0o' + new_num
    case 16:
        print(str(num1) + ' in hex = ' + hex(num1))
        new_num = str(num1) + ' in hex = 0x' + new_num

print(new_num)
