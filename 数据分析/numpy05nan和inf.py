import numpy as np

print(np.nan == np.nan)  # nan不相等
t1 = np.arange(15).reshape(3, 5)
t1 = t1.astype(float)  # nan 为float类型，赋值需转换
t1[2, 3] = np.nan
print(t1)
print(np.count_nonzero(t1))  # 统计非零
print(np.count_nonzero(t1 != t1))  # 统计nan
print(np.isnan(t1))  # 显示bull类型nan
# nan和任何数计算都为nan
'''
sum	计算数组中的和
mean 计算数组中的均值
var	计算数组中的方差
pt[ 计算最大值最小值的差
std	计算数组中的标准差
max	计算数组中的最大值
min	计算数组中的最小值
argmax	返回数组中最大元素的索引
argmin	返回数组中最小元素的索引
cumsum	计算数组中所有元素的累计和
cumprod	计算数组中所有元素的累计积
注意:  每个统计函数都可以按行和列来统计计算;  当 axis=1 时，表示沿着横轴计算;   当 axis=0 时，表示沿着纵轴计算;
'''

# 将数组中nan替换为均值
t1 = np.arange(12, dtype="float").reshape(3, 4)
t1[1, 2:] = np.nan


def Replace(t1):
    for i in range(t1.shape[1]):  # 遍历每一列
        tem_a1 = t1[:, i]  # 当前每一列
        num_nan = np.count_nonzero(tem_a1 != tem_a1)
        if num_nan != 0:  # 不为零，说明这一列有nan
            tem_numnan = tem_a1[tem_a1 == tem_a1]  # 当前一列不为nan的array
            tem_a1[np.isnan(tem_a1)] = tem_numnan.mean()  # 选中nan的位置，为其赋值
    return t1


print(t1)
print(Replace(t1))
