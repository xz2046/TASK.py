import pandas as pd
from matplotlib import pyplot as plt


file_path = 'E:\Python Pycharm\练习\数据分析\练习数据\PM2.5\BeijingPM20100101_20151231.csv'
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', None)  # 显示全部行
#  把分开的时间字符串通过PeriodIndex方法转为pandas的时间类型
period = pd.PeriodIndex(year=df['year'], month=df['month'], day=df['day'], hour=df['hour'], freq='H')
df['datatime'] = period

# 设置索引
df.set_index('datatime', inplace=True)  # True原地修改
df = df.resample('7D').mean()  # 降采样
data = df['PM_US Post'].dropna()  # 删除nan数据

# 画图
x = data.index
# x = [i.strftime('%Y%m%d') for i in x]#格式化时间
y = data.values

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(x)), y, color="m")
plt.xticks(range(0, len(x), 10), list(x)[::10], rotation=45)

plt.show()
