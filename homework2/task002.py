

def zap(n):
    result = 0
    for i in range(1, n+1):
        result += (1+1/i)**i
    print(result)


zap(4)
