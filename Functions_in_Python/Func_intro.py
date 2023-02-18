# Функции

# Пример встроенных функций
# print()
# type()
# len()
# sqrt()
# round()
# upper()

# Задали функцию
def printText():
    print('Hellow world')


printText()  # Вызвали функцию


# Посчитаем площадь круга
def sqRing(r):
    return 3.1415 * (r ** 2)


x = sqRing(10)
print(x)


# Вычислим периметр треугольника
def getSquare(w, h):
    return 2 * (w + h)


print(getSquare(5, 5))


# Формальные параметры в функциях
def printText(msg, end='!'):
    print(msg + end)


printText('Text')
printText('Text', '?')  # Изменили значение формального параметра

# Переопределение существующей функции по ходу работы программы
a = True

if a:  # Если a == True
    def sFunc(x, y, z):
        return x + y + z
else:
    def sFunc(a, b, c, ):
        x = a + b / c
        print(x)

sFunc(10, 20, 30)  # Запустит в зависимости от значения переменной a


# Описание документации к функции
def funct(a, b, c):
    '''
    :param a: Коментарий
    :param b: Переменная
    :param c: Переменная
    :return: Вывод
    '''
    return a + b + c


help(funct)  # Функция вывода документации к функции funct
