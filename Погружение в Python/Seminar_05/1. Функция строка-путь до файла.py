"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def split_file_path(file_path):
    file_name = file_path.split('/')[-1]
    file_parts = file_name.split('.')
    if len(file_parts) == 1:
        file_name = file_parts[0]
        file_ext = ''
    else:
        file_name, file_ext = file_parts[0], file_parts[-1]
    path = '/'.join(file_path.split('/')[:-1])
    return path, file_name, file_ext


print(split_file_path("/Users/xburv/Desktop/Разработчик/Python/file.txt"))
