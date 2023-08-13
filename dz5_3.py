# Создайте функцию генератор чисел Фибоначчи

def gen_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

a=int(input('Введите количество чисел: '))
print(list(gen_fibonacci(a)))