# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.(если получаются длинные числа после запятой,
# это нормально и особенность данного языка программирования.
# Ваш ответ может не совпадать с примером(может получитя 0,20))

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def rez(s):
    for i in range(len(s)):
        s[i] = round(s[i] % 1, 3)
    for i in range(len(s)):
        if s[i] == 0:
            s[i] = max(s)

    print(max(s)-min(s))


rez([1.1, 1.2, 3.1, 5, 10.01])
