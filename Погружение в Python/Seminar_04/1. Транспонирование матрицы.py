"""
Напишите функцию для транспонирования матрицы
"""


def matrix_transp(matrix: [[int]]) -> [[int]]:
    new_matrix = [[]]
    one_string = []
    new_matrix.clear()
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            one_string.append(matrix[j][i])
        new_matrix.append(list(one_string))
        one_string.clear()

    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print('Исходная матрица:')
for i in matrix:
    print(i)

print('Транспонированная матрица:')
for i in matrix_transp(matrix):
    print(i)
