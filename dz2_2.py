# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
from math import gcd

a1, b1 = map(int, input('Введите первое число в формате “a/b” ').split('/'))
a2, b2 = map(int, input('Введите второе число в формате “a/b” ').split('/'))
f_one = Fraction(a1, b1)
f_two = Fraction(a2, b2)


print('Произведение равно ''{}/{}'.format(a1 * a2, b1 * b2))

if b1 == b2:
    print('Сумма равна ''{}/{}'.format(a1+a2, b1))
else:
    cd = int(b1*b2/gcd(b1, b2))
    rn = int(cd/b1*a1+cd/b2*a2)
    g2 = gcd(rn, cd)
    a = int(rn/g2)
    b = int(cd/g2)
    print('Сумма равна ''{}/{}'.format(a, b) if a != b else a)


print('Произведение через модуль fractions равно ',f_one * f_two)
print('Сумма через модуль fractions равно ', f_one + f_two)


    