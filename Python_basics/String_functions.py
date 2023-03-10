# Функции работы с символами
x = 'some long and awesome TEXT'
print(len(x))  # Получить длину строки
print(x[len(x) - 1])  # Обратиться к последнему символу строки
print(x[len(x) - 4:len(x)])  # Получить срез строки
print(x.count('o'))  # Получить количество вхождений символа в строку
print(x.find('o'))  # Получить индекс символа (показывает первый, который попался)
print(x.find('o', 3, 7))  # Получить индекс в диапазоне символов с 3 по 7 индекс
print(x.find('o', 7))  # Получить индекс в диапазоне символов с 7 индекса по конец строки
print(x.find('and'))  # С какого индекса начинается данный текст
print(x.find('hello'))  # Если искомый текст не найден, выдает -1

# Преобразование и регистры
# Важно! Исходная строка остается без изменнений
print(x.capitalize())  # Первый символ - верхний регистр, а остальные - нижний
print(x.upper())  # Все символы в верхнем регистре
print(x.lower())  # Все символы в нижнем регистре
print('Old text: ' + x)  # Исходный текст остался без изменений, не смотря на предыдущие изменения

# Для работы с исходником необходимо присвоить исходный текст в переменную и работать с ней
upper_cased = x.upper()
lower_cased = x.lower()
print(upper_cased.isupper())  # Проверка текста на верхний регистр
print(lower_cased.islower())  # Проверка текста на нижний регистр
print('xxx777'.isalnum())  # Проверка текста, состоит ли он только из букв и цифр (спецсимволы дают False)
print('xxx'.isalpha())  # Проверка тектста, состоит ли он только из букв

# Проверка начала и конец строки на конкретное вхождение
x = str('hello')
print(x.startswith('he'))
print(x.endswith('lo'))

# Функция разделения строки на список строк по определенному разделителю
split = x.split('l')
print(type(split))  # Тип список

# Пример работы с массивом данных, разделенных ';'
some_data = '1;2;3;4;5;6'
list_data = some_data.split(';')
print(list_data)
print(list_data[3])
