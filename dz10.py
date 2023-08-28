# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), 
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра. (Например: Треугольник дз1, дроби дз2)

# Треугольник

class Triangle:
    def __init__(self, a:int, b:int, c:int) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def check(self):
        if self.a + self.b < self.c or self.a + self.c < self.b or self.c + self.b < self.a:
            return "Такого треугольника не существует"
        elif self.a == self.b == self.c:
            return 'Треугольник равносторонний'
        elif self.a != self.b != self.c:
            return 'Треугольник разносторонний'
        else:
            return 'Треугольник равнобедренный'

t1 = Triangle(2, 3, 4)
print(t1.check())
