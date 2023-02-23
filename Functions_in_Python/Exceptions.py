'''
Ошибки и исключения
- Синтаксические ошибки
- Ошибки пользователя
'''

# while True:
#     try:  # Выполняемый код, в котором ожидаем поймать ошибку
#         a = int(input('Введите первое число: '))
#         b = int(input('Введите второе число: '))
#         print(a / b)
#     except ValueError:  # Реагируем на конкретную ошибку, которую предполагаем поймать
#         print('Ошибка! ValueError! Введите число, а не текст!')
#     except ZeroDivisionError:
#         print('Ошибка! ZeroDivisionError! Делить на ноль нельзя!')
#     except Exception as e:  # Учли все возможные ошибки
#         print(e, type(e))  # Выводим ошибку и тип ошибки
#     finally:  # Блок, который в любом случае выполнится
#         print('Операция завершена')

# Пример. Скрипт для проверки лежит сайт или нет
import requests
import time
from datetime import datetime

while True:
    try:
        a = requests.get('https://ya.ru/')
        print(a)
        time.sleep(10)
        if a == '<Response [200]>':
            print('The website is fine!')
        elif a == '<Response [503]>':
            print('Server error')
        else:
            print('Another mistake')
    except requests.exceptions.ConnectionError:
        error_time = datetime.now()
        print('The server is down!\n ' + str(error_time))
        time.sleep(10)
