# Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации.
import logging

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
                logger.info(f'Треугольник равносторонний, со сторонами {self.a} {self.b} {self.c}')
                return 'Треугольник равносторонний'
            elif self.a != self.b != self.c:
                logger.info(f'Треугольник разносторонний, со сторонами {self.a} {self.b} {self.c}')
                return 'Треугольник разносторонний'
            else:
                logger.info(f'Треугольник равнобедренный, со сторонами {self.a} {self.b} {self.c}')
                return 'Треугольник равнобедренный'
        except TypeError as se:
            print('Текст не может быть стороной треугольника')
            logger.error(f'Текст не может быть стороной треугольника. Возникла ошибка {se}')

FORMAT = '{levelname} - {asctime} {msg}'
logging.basicConfig(filename='logger.log',encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger(__name__)

t1 = Triangle(1, 2, 3)
print(t1.check())