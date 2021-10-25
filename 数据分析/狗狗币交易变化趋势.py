import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

file_path = 'E:\Python Pycharm\练习\数据分析\练习数据\DOGE-USD.csv'
df = pd.read_csv(file_path)
pd.set_option('display.float_format', lambda x: '%.6f' % x)  # 解决科学计数法显示的方法一
df['Date'] = pd.to_datetime(df['Date'])  # 将数据中时间转为datetime
df.set_index('Date', inplace=True)  # 将时间那一列作为索引

# 统计每个月狗狗币的交易数量
'''count_m = df.resample('M')
print(count_m['Volume'].sum())'''

# 狗狗币每年交易变化表，取平均值。

count_y = df.resample('Y').mean()[['High', 'Low']]

x = count_y.index
y_h = count_y['High'].values
y_l = count_y['Low'].values
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y_h, label="最高值", color="m")
plt.plot(x, y_l, label="最低值", color="cyan")

plt.ylabel("价值", fontproperties=my_font)
plt.xlabel("年", fontproperties=my_font)
plt.legend(prop=my_font)
plt.title("狗狗币价值变化表", fontproperties=my_font)
plt.savefig('./ooo.png')

plt.show()
