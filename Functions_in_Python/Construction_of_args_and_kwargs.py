# Позиционное присваивание
a, b, c = 'string', 20, 3.14
print(a)
print(b)
print(c)

a, *b, c = 'string', 20, 3.14, 56, 23, 4  # Оператор * распаковывает все лишние значения в отмеченную пмеременную
print(a)
print(b)
print(c)

s = [4, 10]
print(list(range(*s)))  # [4, 5, 6, 7, 8, 9]


def func(a, b, c, d):
    print(a, b, c, d)


a = ('Hello', True, 78, [1, 2, 3])
func(*a)


def func(*args):  # Рапаковывает заранее неизвестное количество неименованных аргументов
    print(sum(args) * 0.06)


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def func(**kwargs):  # Распаковывает заранее неизвестное количество именованных элементов
    print(kwargs)


func(a=1, b=2, c=3)


def func(*args, **kwargs):  # Распаковка в кортеж и словарь
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, '100', a=1, b=2, c=3)
