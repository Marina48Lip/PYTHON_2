# Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь, 
# где ключ — значение переданного аргумента,а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def revers(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            dict[str(value)] = str(key)
        else:
            dict[value] = key
    return dict

print(revers(rev=True, acc="YES", stroka=4, list=[0,1,2]))