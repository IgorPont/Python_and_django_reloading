# Коллекции

new_list = [1, 2, 3, 4, 5]  # Объявил новый список с элементами
mix_list = [12, 3.14, 'text']  # Список может содержать разные типы данных
print(len(new_list))  # Узнать длину списка
print(new_list[0])  # Получить первый элемент списка
print(new_list[-1])  # Получить последний элемент списка
print(new_list[2:])  # Вывести элементы списка начиная с индекса 2 и до конца списка

# Конкатенация и действия со списками

list_1 = ['Igor', 'Vlad', 'Alex']
list_2 = ['Evgen', 'Masha']
print(list_1 + list_2)  # "Сложили" список
list_1[0] = 'Artur'  # Нулевому элементу списка присвоили новое значение
print(list_1)
list_1.append('Anna')  # Добавить в конец списка новый элемент
print(list_1)
list_1.insert(1, 'Jhon')  # Добавить новый элемент на конкретное место по индексу
print(list_1)
print(list_1.index('Anna'))  # Получить индекс конкретного элемента
print(list_1.index('Anna', 0, 5))  # Получить индекс элемента в конкрентном диапазоне (если его нет, то выдаст ошибку)
pop_del = list_1.pop()  # Удалить элемент из списка (без аргументов удаляет последний)
print(pop_del)  # Удаленный элемент присвоен переменной
print(list_1)
list_1.pop(0)  # Удалить конкрентый элемент по индексу
print(list_1)
list_1.clear()  # Очистить список полностью
print(list_1)

# Сортировка списков

list_3 = ['11', '2', '33', '-34', '0']
print(list_3)
list_3.sort()  # Сортировка списка по возрастанию
print(list_3)
list_3.sort(reverse=True)  # Сортировка списка по убываю
print(list_3)

# Сортировка символов

list_4 = ['abcde', 'bcd', 'da', 'cde', 'ser', 'q']
print(list_4)
list_4.sort()  # Обычная сортировка по старшенству
print(list_4)
list_4.sort(key=len)  # Сортировка по ключу (в данном случае - длина значения списка)
print(list_4)
list_4.reverse()  # Реверсировать список - просто отображение списка в обратном порядке (при этом сам список не меняется)
print(list_4)
