import numpy as np

'''
方法:np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)
fname： 文件的名称， 可以是文件名， 也可以是ugz或者bz2的压缩文件;
dtype： 数据类型， 可选， 默认是float;
delimiter： 分隔符字符串， 默认情况是任何的空格，
skiprows: 跳过前xx行， 一般情况跳过第一行;
usecols: 读取指定的列， 可以是元组；
unpack： 如果为True， 对返回的数组对象转置；
'''

t1 = np.arange(100).reshape(20, 5)
print(t1)
print(t1[2])  # 取行
print("-" * 100)
print(t1[18:])  # 连续取行
print("-" * 100)
print(t1[[2, 5, 9]])  # 非连续取行
print("-" * 100)
print(t1[2, :])  # 取行

print("-" * 100)
print(t1[:, 2])  # 取列
print("-" * 100)
print(t1[:, 2:])
print("-" * 100)
print(t1[:, [2, 4]])

print("-" * 100)
a = t1[3, 4]  # 取行列
print(a)
print(type(a))  # 数据类型为数组类型
print("-" * 100)
print(t1[2:4, 1:4])  # 取3到5行，2到5列交叉
print("-" * 100)
print(t1[[0, 2], [0, 1]])  # 取多个不相邻的点（0，0），（2，1）
# 可取步长
print("-" * 100)
# 数据修改
t2 = np.arange(24).reshape(4, 6)
t2[:, 4:] = 0  # 直接赋值
print(t2)
print("-" * 100)
print(t2 < 5)
t2[t2 < 5] = 5  # 小于5的数赋值5，本质是布尔类型ture赋值
print(t2)
n = 3 if 3 < 2 else 4  # 三目运算
print(n)
print("-" * 100)
t3 = np.arange(20).reshape(4, 5)
print(np.where(t3 < 10, 0, 10))  # 把小于10的改为零，大于10的改为10，于三目运算相同
print("-" * 100)
print(t3.clip(10, 18))  # 小于10的替换为10，大于18的替换为18
print("-" * 100)
t3 = t3.astype(float)
t3[3, 3:] = np.nan  # 赋值nan nan为浮点型
print(t3)
