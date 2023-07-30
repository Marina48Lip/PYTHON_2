# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hex_func(number, n):
    digit = '0123456789abcdefgh'
    hex_number = ''
    while number != 0:
        hex_number = digit[number % n] + hex_number
        number //= n
    return hex_number

number = int(input('Введите число: '))

print(hex_func(number, 16))
print(hex(number)[2:])
