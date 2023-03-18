"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

list_array = [1, 1, 1, 1, 6, 7, 7, 8, 2, 2, 2, 3, 3, 4]
duplicate = []

for i in set(list_array):
    if list_array.count(i) > 1:
        print(f'Цифра {i} встречается {list_array.count(i)} раз(а)')
        duplicate.append(i)

print(f'Список с дублирующимися элементами: {duplicate}')
print(f'Список без дубликатов: {set(list_array)}')
