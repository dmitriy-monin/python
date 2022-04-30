# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

list = '5 10 2 7 4 8 9 13'
list2 = []
for i in list.split():
    list2.append(round(int(i)))
print(max(list2), min(list2))