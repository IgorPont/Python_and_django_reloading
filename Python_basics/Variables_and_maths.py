# Переменные
x = 3
print(x)
x = 5
print(x)
y = 4
print(x + y)
print(y + y)
print(x + x)
print(type(x))
z = 'text1234'
print(type(z))
print(z + ' ' + z)
x = None
print(type(x))

# Простые операции
x = 1 + 1
x = 2 - 2
x = 9 / 3  # всегда float
print(9 // 4)  # деление без остатка с округлением
x = 1.2 + 2
x = round(1.2 * 3, 2)
x = 3 % 2
x = 4 % 2 == 0  # True (четное число)
x = 3 % 2 == 0  # False (нечетное число)
x = 2 ** 4  # возведение в степень

# Площадь треугольника

import math

a = 15
b = 11
c = 9

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(round(s, 1))

# Площадь круга

p = 3.14
r = 12

s = p * (r ** 2)
print(s)
