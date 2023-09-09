# Решить задания, которые не успели решить на семинаре.
# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
class TriangleError(Exception):

    def __init__(self, message="Такого треугольника не существует"):
        self.message = message
        super().__init__(self.message)

class Triangle:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        try:
            if self.a + self.b < self.c or self.a + self.c < self.b or self.c + self.b < self.a:
                raise TriangleError()
            elif self.a == self.b == self.c:
                return 'Треугольник равносторонний'
            elif self.a != self.b != self.c:
                return 'Треугольник разносторонний'
            else:
                return 'Треугольник равнобедренный'
        except TypeError:
            print('Текст не может быть стороной треугольника')

t1 = Triangle(3, '1', 3)
print(t1.check())