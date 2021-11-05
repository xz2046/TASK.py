x, y = 1, 0 
def exgcd(a, b):
    global x, y
    if b == 0: 
        x, y = 1, 0
        return a
    d = exgcd(b, a % b)
    x, y = y, x
    y -= (a // b) * x
    return d
    
exgcd(288, 158)
print('a的系数为',x)
print('b的系数为',y)
