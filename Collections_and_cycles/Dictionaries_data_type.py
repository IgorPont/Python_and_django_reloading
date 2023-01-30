# Словари. Тип dict - пара ключ:значение/все ключи уникальны

student = {
    'Alex': 258,
    'Max': 227,
    'Anna': 278
}
print(student)
print(student['Anna'])  # Получить значение по ключу
print(student.get('Anna'))  # Получить значение по ключу с помощью функции get
student['Andrey'] = 268  # Добавить ключ и значение в конец словаря
print(student)
student['Andrey'] = 345  # Присвоить конкретному ключу новое значение
print(student)
student.setdefault('Oleg')  # Добавить новый ключ, но со значением None (если мы не знаем еще значение)
print(student)
student.pop('Oleg')  # Удаление пары по ключу
print(student)
print(student.keys())  # Получить все ключи
print(type(student.keys()))  # Тип ключи словаря
key_list = list(student.keys())  # Преобразовать ключи словаря в список
print(type(key_list))
print(student.values())  # Получить значения ключей
values_list = list(student.values())  # Преобразовать значения ключей в список
print(values_list)
print('Anna' in student)  # Проверка на наличие ключа в словаре
print('Peter' not in student)  # Проверка на отсутствие ключа в словаре
