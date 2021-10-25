import requests, json, datetime
import pandas as pd
from sqlalchemy import create_engine
from app.settings import engine           #从settings中导入engine，用create_engine链接数据库
#engine = create_engine("mysql+pymysql://root:xingzhu2046@localhost:3306/cov?charset=utf8")

class Datascorce():
    def __init__(self):
        data = []   
        times = datetime.datetime.now() 
        today = times.date()                              #获取系统日期 
        time = times.time()                               #获取系统时间
        ltime = engine.execute('select distinct 更新日期 from province;')   #查询数据库中所有日期并去重
        all_dates = ltime.cursor.fetchall()   #获取日期，元组套元组格式            
        for d in all_dates:
            data.append(d[0])
        if datetime.time(0,0,0).__le__(time) and time.__lt__(datetime.time(8,0,0)):  #如果时间在早上八点前用昨天数据
            yesterday = today - datetime.timedelta(days=1)
            self.df = pd.read_sql(f"select * from province where 更新日期='{yesterday}';", engine)
        else:
            if today in data:                   #如果数据库中已有当天数据使用数据库数据
                self.df = pd.read_sql(f"select * from province where 更新日期='{today}';", engine)
            else:                               #爬取网页当天数据并存储到数据库
                self.open_url()
    
    def open_url(self):
        res = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5')
        res_json = json.loads(res.json()['data'])
        area_tree = res_json['areaTree'][0]['children']
        lasttime = res_json['lastUpdateTime'].split(' ')[0]
        total = []
        for child in area_tree:
            a = child['name'], child['today']['confirm'], child['total']['nowConfirm'], child['total']['confirm'],child['total']['dead'],child['total']['heal'],lasttime
            total.append(a)
        name = ['地区', '新增病例','现有病例','累计病例','死亡','治愈','更新日期']
        self.df = pd.DataFrame(columns=name, data=total)
        self.df.to_sql('province', engine, if_exists='append', index=False)

    def get_values(self):
            #转换数据格式，前后端相同
            z = zip(self.df['地区'], self.df['新增病例'], self.df['现有病例'], self.df['累计病例'])
            confirm = []
            nowconfirm = []
            allconfirm = []
            for item in z:
                c = {'name':item[0],'value':item[1]}
                nc = {'name':item[0],'value':item[2]}
                ac = {'name':item[0],'value':item[3]} 
                confirm.append(c)
                nowconfirm.append(nc)
                allconfirm.append(ac)
            return [confirm,nowconfirm,allconfirm]
