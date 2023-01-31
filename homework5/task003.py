

def sjat(vhod):
    a = ''
    result = ''
    for i in range(len(vhod)):
        if a == '':
            a = vhod[i]
            count = 1
        elif a == vhod[i]:
            count += 1
        else:
            result += f'{count}{a}'
            a = vhod[i]
            count = 1
        if i+1 > len(vhod)-1:
            result += f'{count}{a}'
    return result


def vost(text):
    result = ''
    count = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            result += i*int(count)
            count = ''
    return result


def otkr(a):
    data = open(f'{a}', 'r')
    result = data.read()
    data.close
    return result


#  файлы в корневом каталоге


vhod = otkr('file_3(task003).txt')
text = sjat(vhod)
data = open('file_4(task003).txt', 'w')
data.writelines(text)
data.close
print(text)
print(vost(text))
