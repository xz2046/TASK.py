def test(m, n, e):
    n = bin(int(n))
    n = n.replace('0b', '')
    n = n[::-1]
    a = [1]
    b = [int(e)]
    m = int(m)

    cum = 0
    for i in n:
        if int(i) > 0:
            a.append(a[cum]*b[cum] % m)
        else:
            a.append(a[cum] % m)
        if cum < len(n):
            b.append(b[cum] * b[cum] % m)
            cum = cum + 1

    print(a[cum])


m =input("请输入模数m: ")
b =input("请输入幂: ")
a =input("请输入底数: ")
test(m, b, a)