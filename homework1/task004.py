# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def num():
    a = False
    while not a:
        result = int(input("Введите номер четверти: "))
        if 5 > result > 0:
            a = True
    return result


def axis(a):
    if a == 1:
        print('x > 0, y > 0')
    elif a == 2:
        print('x < 0, y > 0')
    elif a == 3:
        print('x < 0, y < 0')
    elif a == 4:
        print('x > 0, y < 0')


axis(num())
