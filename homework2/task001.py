
def numb(n):
    s = str(n)
    result = 0
    for i in s:
        if not (i == "."):
            result += int(i)
    return result


print(numb(6782))
