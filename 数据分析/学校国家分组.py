import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

file_path = 'E:\Python Pycharm\练习\数据分析\练习数据\school_and_country_table.csv'
df = pd.read_csv(file_path)
# print(df.info())

data1 = df.groupby(by='country').count().sort_values(by='school_name', ascending=False)  # ascending 降序，升序
data1 = data1.head(10)
print(data1)
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
plt.figure(figsize=(20, 9), dpi=100)

x_ = data1.index
y_ = data1['school_name'].values

plt.bar(range(len(x_)), y_)
plt.xticks(range(len(x_)), x_)

plt.show()
