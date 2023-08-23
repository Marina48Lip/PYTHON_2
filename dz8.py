# Напишите функцию, которая сереализует содержимое текущей директории в json-файл.
# В файле должен храниться список словарей, словарь описывает элемент внутри директории:
# имя, расширение, тип. Если элемент - директория, то только тип и имя. 
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]


import os
import json


def file_to_list(list):
    list = []   
    with os.scandir() as files:
        for file in files:
            if file.is_file():
                name, ext = file.name.split('.')
                file_dict = dict([('name', name), ('extension', ext), ('type', 'file')])  
                list.append(file_dict)
            else:     
                dir_dict = dict([('name', file.name), ('type', 'directory')])
                list.append(dir_dict)
    return list
  
def list_to_json(filename: str = 'file_to_json.json'):
    with open(filename, 'w') as f:
        data = json.dump(file_to_list(list), f, indent=4)


list_to_json()
print(file_to_list(list))


