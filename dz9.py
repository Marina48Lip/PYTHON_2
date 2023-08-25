# Создать декоратор для использования кэша. 
# Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами,
# которые уже записаны в кэше - вернуть результат из кэша, 
# если нет - выполнить функцию. Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.

import json
from typing import Callable

def json_logging(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            result_list = json.load(data)
    except FileNotFoundError:    
        result_list = []
    
    def wrapper(*args, **kwargs):
        result = func(*args)
        for i in range(len(result_list)):
            if result_list[i]['num '] == num:
                return print(f'Сумма данного числа есть в кеше и равно {result}')   
                
        result_list.append({'num ': num,
                            'summ ': result})
        with open(f'{func.__name__}.json', 'w') as data:
            json.dump(result_list, data, indent=4)
        print(result_list)
        return result
    return wrapper

@json_logging
def sum_args(*args):
    return (num + num)

if __name__ == '__main__':
    num = int(input("Введите число "))
    sum_args(num)