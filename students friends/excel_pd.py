import pandas as pd
import xlrd

df1 = pd.read_excel('E:\Python Pycharm\练习\students friends\excel\招生名单.xls')
df2 = pd.read_excel('E:\Python Pycharm\练习\students friends\excel\招生名单 (2).xls')
df3 = pd.read_excel('E:\Python Pycharm\练习\students friends\excel\招生名单（3）.xlsx')

df = pd.concat([df1, df2, df3])
df = df[pd.notnull(df['姓名'])]

