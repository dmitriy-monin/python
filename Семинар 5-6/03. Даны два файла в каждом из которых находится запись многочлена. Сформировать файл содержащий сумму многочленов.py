# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.
 
f = open('task_2.txt', 'r')
list_main = []
 
for str in f:
    list_main.append(str)
 
list_str_0 = list_main[0].split(' ')
list_str_1 = list_main[1].split(' ')
 
f_list_edit = lambda lis: [i for i in lis if i not in {'+', '=', '0\n', '0'}]
print(list_str_0 := f_list_edit(list_str_0))
print(list_str_1 := f_list_edit(list_str_1))
print()
 
 
def higher_degree_in_str(li):
    for i in li:
        num = (i.index('^'))
        num = int(i[num + 1:])
        break
    return num
 
 
higher_degree_0 = higher_degree_in_str(list_str_0)
higher_degree_1 = higher_degree_in_str(list_str_1)
 
 
def more_less(li, x, y):
    while x - y != 0:
        li.reverse()
        li.append('0')
        li.reverse()
        x -= 1
    return li
 
 
if higher_degree_0 > higher_degree_1:
    list_str_1 = more_less(list_str_1, higher_degree_0, higher_degree_1)
else:
    list_str_0 = more_less(list_str_0, higher_degree_1, higher_degree_0)
 
 
def list_number(li, l):
 
    list_format = []
    for i in li:
 
        if i not in li[-1]:
            if '^' not in i:
                list_format.append((int(i)))
            else:
                num_end = i.index('^')
                num_end = int(i[num_end + 1:])
 
                num_start = i.index('*')
                num_start = int(i[0: num_start])
 
                while l - num_end >= 1:
 
                    list_format.append(0)
                    l -= 1
 
                list_format.append(num_start)
                l -= 1
 
        else:
            if '^' not in i:
                list_format.append(int(i))
            else:
                num_end = i.index('^')
                num_end = int(i[num_end + 1:])
 
                num_start = i.index('*')
                num_start = int(i[0: num_start])
 
                while l - num_end >= 1:
                    list_format.append(0)
                    l -= 1
 
                while num_end != 1:
                    list_format.append(0)
 
                list_format.append(num_start)
                list_format.append(0)
 
    return list_format
 
 
print(list_str_0_format := list_number(list_str_0, higher_degree_0))
print(list_str_1_format := list_number(list_str_1, higher_degree_1))
 
list_m = [x+y for x, y in zip(list_str_0_format, list_str_1_format)]
print()
print(f'final: {list_m}')