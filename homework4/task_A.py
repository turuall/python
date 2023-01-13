# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2x² + 4x + 5 = 0
#  или x² + 5 = 0
#  или 10*x² = 0

import random


def kof():
    return random.randint(0, 100)


k = 2
result = ''
for i in range(k, -1, -1):
    a = kof()
    if a != 0:
        if i != 0:
            result += f'+{a}x^{i}'
        else:
            result += f'+{a}'
result += '=0'
data = open('task_A.txt', 'a')
data.write(result)
data.close
