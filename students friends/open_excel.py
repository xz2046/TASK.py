import pandas as pd
import pymysql
from sqlalchemy import create_engine

df = pd.read_excel('E:\Python Pycharm\练习\students friends\student_data.xlsx')
df = df.loc[ : , ~df.columns.str.contains("^Unnamed")]
engine = create_engine("mysql+pymysql://root:xingzhu2046@localhost:3306/friend?charset=utf8")

df.to_sql(name='student_data', con=engine, if_exists='append', index=False, index_label=False)
