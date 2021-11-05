def sushu(n):
    result = []
    for x in range(2,n+1):
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            result.append(x)
    return result  

print('30以内素数有：',sushu(30))