import string

import pandas as pd

t1 = pd.Series([1, 5, 9, 45, 3, 5, 1, 96])
print(t1, type(t1))
print("_" * 100)
t2 = pd.Series([1, 25, 68, 34, 37], index=list("abcde"))  # index指定索引
print(t2)
print("_" * 100)
d1 = {"name": "xiaoming", "age": 18, "tel": "10086"}
t3 = pd.Series(d1)  # 通过字典创建
print(t3)
print("_" * 100)
d2 = {string.ascii_uppercase[i]: i for i in range(10)}
print(d2)
t4 = pd.Series(d2, index=list(string.ascii_uppercase[5:15]))
print(t4)
print("_" * 100)
# 切片与索引
print(t3["age"])
print(t3[1])
print(t3[:2])
print("_" * 100)
print(t3[[0, 2]])
print("_" * 100)
print(t3[["age", "tel"]])
print(t1[t1 > 5])
print("_" * 100)
print(t4.index)  # key
for i in t4.index:
    print(i)
s1 = list(t4.index)[:3]
print(s1)
print(t4.values)  # 键值
t5 = pd.Series([1, 2, 3, 4, 5, 6])
print(t5.where(t5 > 2))  # where方法
print(t5.where(t5 > 2, 10))
