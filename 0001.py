import pandas as pd
from sqlalchemy import create_engine
import pandas_alive
import datetime
times = datetime.datetime.now()
today = times.date()

engine = create_engine("mysql+pymysql://root:xingzhu2046@localhost:3306/cov?charset=utf8")
df = pd.read_sql('select * from chinadate;',engine)

df['日期'] = df['日期'].astype('datetime64')
df.set_index('日期', inplace=True)

df2 = df[['累计确诊','简称']].groupby('日期')

name = list(set(df['简称'].tolist()))
df3 = pd.DataFrame(index=(pd.date_range('2020-01-19',today)),columns=name).fillna(0)
for i in df2:
    data = list(zip(i[1].index,i[1]['简称'],i[1]['累计确诊']))
    for j in data:
        df3.loc[j[0],j[1]] = j[2]  
covid_df = pandas_alive.load_dataset(df3)
covid_df.plot_animated(filename='0001.gif',perpendicular_bar_func='mean')
