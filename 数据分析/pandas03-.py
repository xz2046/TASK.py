import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("XYZW"))
print(df.loc[:, "Y"])  # loc取坐标，iloc取位置
print(df.loc["a", "X"])
print(df.iloc[:, 1])
df.loc["a", "X"] = np.nan
print(df)
# 判断数据是否为nan
print(pd.isnull(df))
print(pd.notnull(df))
df1 = df.copy()
print("=" * 100)
df2 = df.dropna(axis=0, how="any", inplace=False)  # any为任何nan都删除，all为一行全为nan才删除
print(df2)
df3 = df1.fillna(df1.mean())  # 填充均值
print(df3)
print("=" * 100)
df4 = df.copy()
df4["X"] = df4["X"].fillna(df4["X"].mean())
print(df4)
