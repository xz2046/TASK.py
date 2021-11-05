a = int(input('请输入被除数:'))
b = int(input('请输入除数:'))
if b == 0:
    b = int(input('除数不能为零，请重新输入:'))
else:
    c = a//b
    d = a%b
    print(f'{a}={b}✖{c}+{d}')