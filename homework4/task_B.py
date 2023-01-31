# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def otkr(a):
    data = open(f'{a}', 'r')
    result = data.read()
    data.close
    return result


def razl(st):
    st = st.replace('=0', '')
    rezult = st.split('+')
    kof = [0, 0, 0]
    for i in range(len(rezult)):
        if 'x^2' in rezult[i]:
            rezult[i] = rezult[i].replace('x^2', '')
            kof[0] = int(rezult[i])
        elif 'x^1' in rezult[i]:
            rezult[i] = rezult[i].replace('x^1', '')
            kof[1] = int(rezult[i])
        else:
            kof[2] = int(rezult[i])
    return kof

 
# Файлы 1 и 2 находятся  в корневом каталоге
 
a = razl(otkr('file_1(task_b).txt'))
b = razl(otkr('file_2(task_b).txt'))
c = list(map(sum, zip(a, b)))

data = open('task_B.txt', 'a')
data.write(f'{c[0]}x^2+{c[1]}x^1+{c[2]}=0')
data.close