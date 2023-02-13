# Цикл while

import time

# x = 1
# while True:
#     x = x + x
#     print(x)
#     time.sleep(1) # перерыв между операциями

x = 0
while x < 6:
    print(f'X равно {x}')
    x += 1
    time.sleep(0.5)
else:
    print('Завершено')

# Continue (переходим к следующему действию),
# break(останавливаем цикл),
# pass(ничего не делаем)

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for x in vals:
    if x % 2 == 0:
        continue
    else:
        sum += x
    if sum > 10:
        break
print(sum)

while True:
    pass  # Заполнитель пустого цикла, в данном цикле не будет ничего происходить
