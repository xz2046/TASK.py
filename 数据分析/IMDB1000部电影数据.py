import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 数据合并： join merge  https://blog.csdn.net/weixin_38168620/article/details/80663892

file_path = "E:\Python Pycharm\练习\数据分析\练习数据\movie_metadata.csv"
df = pd.read_csv(file_path)
temp_list = df["genres"].str.split("|").tolist()  # 统计电影类型分类
grnres_list = list(set([i for j in temp_list for i in j]))  # 统计所有类型

zero_df = pd.DataFrame(np.zeros((df.shape[0], len(grnres_list))), columns=grnres_list)  # 创建等大的全零数组
# print(zero_df)

for i in range(df.shape[0]):
    zero_df.loc[i, temp_list[i]] = 1  # 给出现分类的地方赋值为1 这个循环太妙了
# print(zero_df.head(3))

# 统计所有类型的电影的数量和
geners_sum = zero_df.sum(axis=0)
# print(geners_sum)
geners_sum = geners_sum.sort_values()  # 排序

# 画图
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
plt.figure(figsize=(20, 9), dpi=100)

x = geners_sum.index
y = geners_sum.values

plt.barh(x, y, height=0.5, color="cyan")
plt.xlabel("类型", fontproperties=my_font)
plt.ylabel("数量", fontproperties=my_font)
plt.title("5000部电影类型数量统计", fontproperties=my_font)
plt.xticks(range(0, 3000, 100))

plt.grid(alpha=0.6)
plt.savefig("./5000部电影类型数量统计.png")
plt.show()

'''df1 = df.loc[:, ["导演姓名", "期间", "导演脸书", "总计", "年份", "喜欢人数"]]
print(df1)
print(df1[(80000 < df1["喜欢人数"]) & (100000 > df1["喜欢人数"])])
print(df1.info())
print(df1[(80000 < df1["喜欢人数"]) & (100000 > df1["喜欢人数"]) & (df1["导演姓名"].str.len() > 8)])'''
