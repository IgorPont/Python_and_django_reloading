# Функция map описание (название функции в параметрах указывается без скобок)
def map(func, iterible):  # map object, который можно преобразовать
    for i in iterible:
        yield func(i)


# Пример
def sq(x):
    return x ** 2


a = [1, 2, 3, 4, 5]

b = map(sq, a)
print(b)  # map object
print(list(b))  # Преобразовали из map object в список

# Еще пример
a = ['hello', 'abc', 'good']
b = list(map(str.upper, a))  # Применили к элементам списка a функцию str.upper
print(b)

# Функция filter фильтрует элементы и выдает те, которые не проходят проверку
age = [11, 20, 18, 33, 14, 12]


def is_adalt(age):
    return age >= 18


f = list(filter(is_adalt, age))  # Вывели значения, которые проходят условие
print(f)

# Анонимная lambda функция
# Перепишем функции выше с помощью lambda
a = [1, 2, 3, 4, 5]

print(list(map(lambda x: x ** 2, a)))

age = [11, 20, 18, 33, 14, 12]


def is_adalt(age):
    return age >= 18


print(list(filter(lambda age: age >= 18, age)))
