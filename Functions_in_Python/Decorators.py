'''
Декоратор - функция, которая принимает другую функцию и расширяет ее функционал
без из менения последней (как переопределение в java)

Конструкция.
tag1 = tagMaker(printText)
def tagMaker(func): # где funk = printText
    def wrapper(*args, **kwargs):
        оператор до функции
        вызов функции func
        оператор после функции
    return wrapper
'''


def tagMaker(func):
    def wrapper(*args,
                **kwargs):  # Так как не знаем количество входных параметров, указали неименованные и именованные аргументы
        print('<div>')
        func(*args, **kwargs)  # Функция, которую переопределяем
        print('</div>')

    return wrapper


@tagMaker  # Обозначение для запуска функции через декоратор
def printText(text):
    print(text)


printText('hello world')

# Пример (подсчет работы времени функции)
import time
import datetime
from functools import wraps  # декоратор для декоратора, чтобы функция help ссылалась на саму функцию, а не на декоратор


def recTime(func):
    @wraps(func)  # для ссылки на саму функцию, а не на декоратор
    def wrapper(*args, **kwargs):
        '''
        Функция, которая считает время работы других функций
        '''
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now() - start
        print(f'Функция завершена за {done} сек')

    return wrapper


@recTime
def sfunc():
    '''
    Функция, которая ждет 3 сек
    '''
    time.sleep(3)
    print('Завершено')


help(sfunc)  # Ссылка идет не данную функцию, а на декоратор
