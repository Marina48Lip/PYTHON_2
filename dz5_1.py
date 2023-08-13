# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os
line = input("Введите путь до файла: ")

def dec_path (line):
    dirname = os.path.splitext(os.path.dirname(line)+'/')
    name = os.path.splitext(os.path.basename(line))
    line1 = dirname + name
    line_list = list(line1)
    line_list.pop(1)
    return line_list

print(tuple(dec_path(line)))


