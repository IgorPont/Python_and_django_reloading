# Множества - последовательность уникальных объектов
# (не поддерживает обращение по индексу)

first_set = {'Aleks', 'Jhon', 'Georg',
             'Aleks'}  # Объявили множество (два раза Aleks указано специально, повторы не учитываются)
print(type(first_set))  # Тип множество
print(first_set)  # {'Jhon', 'Georg', 'Aleks'}
print(len(first_set))  # 3
first_set.add('Max')  # Добавить элемент во множество
print(first_set)
print('Max' in first_set)  # Проверка наличия элемента во множестве - True
first_set.remove('Aleks')  # Удалить элемент множества
print(first_set)
first_set.clear()  # Очистить множество полностью
print(first_set)

# Слияние (объединение) множеств

first_set = {'Aleks', 'Jhon', 'Georg', 'Aleks'}
second_set = {'Anton', 'Tom', 'Anna', 'Aleks'}
third_set = first_set.union(second_set)  # Объединение = первое множество + второе множество - дубликаты элементов
print(third_set)
fourth_set = first_set.intersection(
    second_set)  # Пересечение = элементы, которые присутствуют в первом и во втором множествах
print(fourth_set)
fifth_set = first_set.difference(
    second_set)  # Разность = только множества, которые присуствуют в первом, но отсутствуют во втором
print(fifth_set)
print(first_set - second_set)  # Аналогично операции разности множеств

# Проверка содержания элементов одного множества во втором

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(set_1.issubset(set_2))  # True (все элементы первого множества содержатся во втором множестве)
print(set_2.issuperset(set_1))  # True (первое множество является подмножеством второго)
print(set_1[0])  # Ошибка - множества не поддерживают обращение к элементу по индексу
