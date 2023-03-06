# Магические (Dunder) методы для строкового представления объекта класса
'''
Метод возвращает строковое представление заданного атрибута класса
Для вывода на сайт лучше использовать __str__:
def __str__(self):
    return self.atr

Для вывода в лог файл лучше использовать __repr__:
def __repr__(self):
    return self.atr
'''


class New():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return self.name


new_obj = New('Alex')
print(new_obj)
