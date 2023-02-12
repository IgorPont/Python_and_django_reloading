# Цикл for

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in numbers:
    print(i)
    print(i * i)  # Операции с элементами списка

# Функция range()
numbers = range(1, 6)  # 6 не входит
new_list = []
for i in numbers:
    new_list.append(i)  # Заполняем список числами
print(new_list)

# Ветвления в цикле
for i in range(1, 16):
    if i % 2 == 0:
        print(f'Число {i} - четное число')
    else:
        print(f'Число {i} - нечетное число')

# Работа с индексами элементов списка через функцию enumerate()
num = [1, 2, 3, 4, 5]

for x, item in enumerate(num):
    num[x] += 10
print(num)

# Итерация по строке

name = 'Alex Jhonson'
for i in name:
    print(i)

for _ in range(1, 5):  # Символ подчеркивания используется, чтобы не вводить переменную
    print('Ошибка!!!')

# Работа с кортежем в цикле
some_tuple = (11, 'Alex', 3.14)

for i in some_tuple:
    print(i)

# Работа со списком кортежей
some_list = [('John', 22), ('Alex', 33)]

for (name, age) in some_list:
    print(f'{name} is {age} years old')

# Работа со словарем
some_dict = {
    'Alex': 111,
    'Bob': 333
}

for i in some_dict:  # Прошлись по ключам
    print(i)

for x, y in some_dict.items():  # Прошлись по ключу и значению
    print(f'Ключ {x} и Значение {y}')

for value in some_dict.values():  # Прошлись только по переменным
    print(value)
