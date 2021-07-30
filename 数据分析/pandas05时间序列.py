import pandas as pd

dt = pd.date_range(start='20201001', end='20201101', freq='D')
print(dt)  # start开始时间，end结束时间，freq频率D天M月Y年
'''
B	工作日频率
C	自定义工作日频率
D	日历日频率
W	每周频率
M	每月最后一个日历日
SM	每半个月最后一个日历日（15日和月末）
BM	每月最后一个工作日
CBM	自定义每月最后一个工作日
MS	每月第一个日历日
SMS	每半月第一个日历日（第1和第15）
BMS	每月第一个工作日
CBMS	自定义每月第一个工作日
Q	每季度最后一个月的最后一个日历日
BQ	每季度最后一个月的最后一个工作日
QS	每季度最后一个月的第一个日历日
BQS	每季度最后一个月的第一个工作日
A, Y	每年的最后一个日历日
BA, BY	每年的最后一个工作日
AS, YS	每年的第一个日历日
BAS, BYS	每年的第一个工作日
BH	工作日按“时”计算频率
H	每小时频率
T, min	每分钟频率
S	每秒频率
L, ms	毫秒频率
U, us	微秒频率
N	纳秒频率'''
print('_' * 100)
dt1 = pd.date_range(start='20201001', end='20201101', freq='10D')
print(dt1)
print('_' * 100)
dt2 = pd.date_range(start='20201001', periods=10, freq='M')
print(dt2)  # periods个数
print('_' * 100)
list_obj = ['20201101', '2020-10-01', '2020/01/01']
dt3 = pd.to_datetime(list_obj)
print(dt3)

# resample('M') 可以转换频率
