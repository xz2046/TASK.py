from sqlalchemy.ext.declarative import declarative_base   #数据库建模
from sqlalchemy import Column,VARCHAR,INTEGER,Date
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:xingzhu2046@localhost:3306/cov?charset=utf8")
Base = declarative_base()

class Province(Base):
    __tablename__ = 'chinaDate'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    日期 = Column(Date)
    省份 = Column(VARCHAR(50))
    累计确诊 = Column(INTEGER)
    每日确诊 = Column(INTEGER)
    累计治愈 = Column(INTEGER)
    每日治愈 = Column(INTEGER)
    现存确诊 = Column(INTEGER)
    现存确诊变化 = Column(INTEGER)
    累积死亡 = Column(INTEGER)
    每日死亡 = Column(INTEGER)
    累计可疑 = Column(INTEGER)
    每日可疑 = Column(INTEGER)
    简称 = Column(VARCHAR(30))



if __name__ == '__main__':
    #创建表格
    Base.metadata.create_all(engine)
