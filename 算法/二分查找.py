num = int(input('输入查找数字：'))
l = input('请输入列表：').split(',')
l1 = sorted([int(l[i]) for i in range(len(l))])
def chazhao(num,l1):
    while len(l1)>1:
        mid = len(l1)//2
        if num == l1[mid]:
            print('找到了',num)
            break
        elif num < l1[mid]:
            l1 = l1[:mid]
            print(l1)
            chazhao(num,l1)
        elif num > l1[mid]:
            l1 = l1[mid:]
            print(l1)
            chazhao(num,l1)
    else:
        print('没有啊')
    
chazhao(num,l1)