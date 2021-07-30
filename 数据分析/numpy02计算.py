import numpy as np

t9 = np.arange(12)
print(t9.shape)  # 查看数据形状
print(t9.reshape(3, 4))  # 更改数据形状  #方法有返回值，不会改变数据

t10 = np.arange(24).reshape(2, 3, 4)  # 三维数组
print(t10)
print(t10.reshape(24, ))  # 改为一维数组
print("-" * 100)
t11 = t10.reshape((t10.shape[0] * t10.shape[1] * t10.shape[2]), )  # 不知道数据长度情况下改为一维数组方法一
print(t11)
print("-" * 100)
print(t10.flatten())  # 不知道数据长度情况下改为一维数组方法二
print("-" * 100)
t12 = np.arange(12).reshape(3, 4)
print(t12)
print("-" * 100)
print(t12 + 5)  # 数组中每个数加5乘除同理
print("-" * 100)
print(t12 / 0)  # RuntimeWarning警告  nan数据缺失 inf（inf和-inf）正负无穷
print("-" * 100)
t13 = np.arange(100, 112).reshape(3, 4)
print(t12 + t13)  # 同位相加,乘除同理
print("-" * 100)
t14 = np.array([0, 1, 2, 3])
print(t12 - t14)  # 每行相减
print("-" * 100)
t15 = np.arange(3).reshape(3, 1)
print(t12 - t15)  # 每列相减
'''
shape(2,2,3)可以和shape(2,3)、shape(2,1)、shape(1,3)、shape(1,2,3)运算
广播原则:
让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐
输出数组的形状是输入数组形状的各个维度上的最大值
如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错
当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值
'''
print("-" * 100)
t16 = np.arange(12).reshape(3, 4)
print(t16)
print(t16.transpose())  # 对角线转置  方法一
print("-" * 100)
print(t16.T)  # 转置方法二
print("-" * 100)
print(t16.swapaxes(1, 0))  # 交换轴 转置方法三
