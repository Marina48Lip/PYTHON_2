# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

import sys



def date_check(day, month, year):
    
    day_31 =[1, 3, 5, 7, 8, 10, 12]
    day_30 =[4,6,9,11]
    if 1 <= day <= 31 and month in day_31 and 1<= year <= 9999:
        print('Такая дата существует')
        return True
    elif 1 <= day <= 30 and month in day_30 and 1<= year <= 9999:
        print('Такая дата существует')
        return True
    elif 1<= day <= 29 and month == 2 and vis_year(year):  
         print('Такая дата существует')
         return True
    elif 1 <= day <= 28 and month == 2 and 1<= year <= 9999:
        print('Такая дата существует')
        return True
    else:
        print('Такая дата не существует')
        return False

def vis_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'Високосный год'
    else:
        return 'Год не високосный'


date = input('Введите дату в формате DD.MM.YYYY: ')
day, month, year = map(int, date.split('.'))
print(date_check(day, month, year))    
print(vis_year(year))


if __name__ == '__main__':
    _, day, month, year = sys.argv
    date_check(int(day), int(month), int(year))