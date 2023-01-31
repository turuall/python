# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

def hod(a, znach):
    return str(input(f'{a} : '))


def prov(znach):
    return znach['1'] == znach['2'] == znach['3'] or znach['4'] == znach['5'] == znach['6'] or znach['7'] == znach['8'] == znach['9'] or znach['1'] == znach['4'] == znach['7'] or znach['2'] == znach['5'] == znach['8'] or znach['3'] == znach['6'] == znach['9'] or znach['1'] == znach['5'] == znach['9'] or znach['3'] == znach['5'] == znach['7']


znach = {'1': 1, '2': 2, '3': 3, '4': 4,
         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
print(f"{znach['1']} | {znach['2']} | {znach['3']} \n{znach['4']} | {znach['5']} | {znach['6']} \n{znach['7']} | {znach['8']} | {znach['9']}")
win = None
while win == None:
    znach[hod('Ходит 1 игрок', znach)] = 'X'
    print(f"{znach['1']} | {znach['2']} | {znach['3']} \n{znach['4']} | {znach['5']} | {znach['6']} \n{znach['7']} | {znach['8']} | {znach['9']}")
    if prov(znach):
        win = 'Выйграл 1 игрок'
    else:
        znach[hod('Ходит 2 игрок', znach)] = 'O'
        print(f"{znach['1']} | {znach['2']} | {znach['3']} \n{znach['4']} | {znach['5']} | {znach['6']} \n{znach['7']} | {znach['8']} | {znach['9']}")
        if prov(znach):
            win = 'Выйграл 2 игрок'
print(win)
