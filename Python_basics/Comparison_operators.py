# Булево значение

x = int(True)  # 1
print(x)

y = int(False)  # 0
print(y)

a = []  # пустая строка возвращает False
b = [1, 2, 3]
x = bool(a)
print(x)
print(bool(b))

# Операторы сравнения
print(2 > 3)
print(3 < 2)
print(2 > 1)
print(2 >= 2)
print(3 >= 2)
print(2 >= 3)
print(2 != 1)
print(1 == 1)
print('text' == 'text')  # важен регистр
print(1 < 2 < 3 < 4 < 5)  # логическая цепочка, если один False? то и вся цепочка - False
print(1 < 2 and 2 < 3)  # True
print(1 < 2 or 2 > 3)  # True
