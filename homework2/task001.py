#  Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

#  Пример:
#  6782 -> 23
#  0,56 -> 11


def numb(n):
    s = str(n)
    result = 0
    for i in s:
        if not (i == "."):
            result += int(i)
    return result


print(numb(6782))
