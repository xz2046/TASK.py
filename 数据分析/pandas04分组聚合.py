import pandas as pd
import numpy as np

dict_obj = {'key1': ['a', 'b', 'a', 'b',
                     'a', 'b', 'a', 'a'],
            'key2': ['one', 'one', 'two', 'three',
                     'two', 'two', 'one', 'three'],
            'data1': np.random.randn(8),
            'data2': np.random.randn(8)}
df_obj = pd.DataFrame(dict_obj)
print(df_obj)

df2 = df_obj.groupby("key1")
print(df2.mean())  # 对GroupBy对象进行分组运算/多重分组运算，如mean()
print(df2.size())  # size() 返回每个分组的元素个数

df3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("XYZM"))
print(df3)
print("*" * 100)
grouped = df3.groupby(by=[df3["X"], df3["Z"]]).count()  # 按多行分组
print(grouped)

print("*" * 100)
print(df3["X"])
print(df3[["X"]])  # 一列依旧是df格式
print(type(df3[["X"]]))
print("*" * 100)
# 索引的属性
print(grouped.index)
# 索引赋值
df3.index = ["A", "B", "C"]
print(df3)
print("*" * 100)
df4 = pd.DataFrame(np.arange(10).reshape(2, 5), index=["a", "b"], columns=list("qwert"))
df_1 = df4.reindex(["a", "c"])  # 重新设置index 以前有的保持，没有的变为nan
print(df_1)

print(df4.set_index("q", drop=True))  # 指定某一列为索引 drop为true把指定索引的列从中删掉，false，保留
print(df4.index.unique())  # 返回索引中的唯一值，去重

print("*" * 100)
dict_1 = {"a": range(7), "b": range(7, 0, -1), "c": ["one", 'one', 'one', 'two', 'two', 'three', 'three'],
          'd': list('hijklmn')}
df6 = pd.DataFrame(dict_1)
df_2 = df6.set_index(["c", "d"])
print(df_2)
print(df_2.index)
print('_' * 100)
a = df_2["a"]
print(a)
print(a["one"]["j"])
print('-' * 100)
df_3 = df6.set_index(['d', 'c'])
b = df_3['a']
print(b.swaplevel())  # 交换索引
print(b.swaplevel()['one'])  # 从内层开始取索引

print('-' * 100)
print(df_2.loc['one'].loc['h'])#复合索引取值
print(df_2.swaplevel().loc['h'])#从内层取索引