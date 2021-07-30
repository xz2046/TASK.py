import numpy as np
import pandas as pd

# https://www.cnblogs.com/chenhuabin/p/11477076.html#_label1_0  读取数据方法

t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("XYZN"))
print(t1)  # datafarme  其实是个series容器，行列单独拆开都为一个series类型数组
print("-" * 100)
d1 = {"name": ["小米", "小花", "小河"], "age": ["12", "18", "32"], "tel": ["10086", "10010", "10000"]}
t2 = pd.DataFrame(d1)
print(t2)
print(t2.describe())  # 快速统计数据
print("-" * 100)
d2 = [{"name": "xiao", "age": 12, "tel": "10086"}, {"name": "zhong", "tel": "10010"}, {'name': "da", "age": 18}]
t3 = pd.DataFrame(d2)
print(t3)
print("-" * 100)
print(t3.index)
print(t3.columns)
print(t3.values)
print(t3.shape)
print(t3.dtypes)
print(t3.ndim)  # 数据维度
print("-" * 100)
t4 = pd.read_csv("豆瓣TOP250电影.txt", sep="\t", header=0)
print(t4)
print(t4.head())  # 显示头几行数据，默认参数是5
print(t4.tail())  # 显示尾部
print(t4.info())  # 数组信息概览
