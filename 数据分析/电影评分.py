import pandas as pd

file_path = 'E:\Python Pycharm\练习\数据分析\练习数据\movie_metadata.csv'

df = pd.read_csv(file_path)


data = df[pd.notnull(df['年份'])]#去除nan的行
data1 = data.groupby(by='年份').count()['喜欢人数']
print(data1)