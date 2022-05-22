# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9

string = '8/2*3+4*3-7*1'
list = []

for i in string:
    if i.isdigit() == True:
        list.append(int(i))
    elif i == '+':
        list.append('+')
    elif i == '-':
        list.append('-')
    elif i == '*':
        list.append('*')
    elif i == '/':
        list.append('/')
print(f'Задано выражение: {list}')

case = ('*', '/', '+', '-')
temp = 0
list_2 = []
res = []

for i in range(len(list)):
    if i == len(list):
        break
    if list[i] == case[0] or list[i] == case[1]:
        if list[i] == case[0]:
            temp = list[i - 1] * list[i + 1]
            x = list.pop(i - 1)
            list[i] = temp
            x = list_2.pop(-1)
            list_2.append(temp)
            continue
        else:
            temp = list[i - 1] / list[i + 1]
            x = list.pop(i - 1)
            list[i] = temp
            x = list_2.pop(-1)
            list_2.append(temp)
            continue
    list_2.append(list[i])

print(f'Проведено умножение и деление: {list_2}')

for j in range(len(list_2)):
    if j == len(list_2):
        break
    if list_2[j] == case[2] or list_2[j] == case[3]:
        if list_2[j] == case[2]:
            temp = list_2[j - 1] + list_2[j + 1]
            list_2[j + 1] = temp
            x = list_2.pop(j - 1)
            res.pop(-1)
            res.append(temp)

        else:
            temp = list_2[j - 1] - list_2[j + 1]
            list_2[j + 1] = temp
            x = list_2.pop(j - 1)
            res.pop(-1)
            res.append(temp)
        continue

    res.append(list_2[j])

print(f'Результат выражения: {res}')