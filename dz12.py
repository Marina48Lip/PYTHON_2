# Задание 1. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

class Descriptor:
    
    def check(self, value: str):
        if value != value.capitalize() or not value.isalpha():
            raise TypeError(
                'ФИО должны начинаться с заглавной буквы и содержать только буквы')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check(value)
        setattr(instance, self.name, value)


class Student:
    firstname = Descriptor()
    lastname = Descriptor()
    patronim = Descriptor()

    def __init__(self, firstname, patronim, lastname) -> None:
        self.firstname = firstname
        self.patronim = patronim
        self.lastname = lastname

if __name__ == '__main__':
    s1 = Student('Иван', 'Иванович', 'Иванов')
    print(s1.firstname + " " + s1.patronim + " " + s1.lastname)
