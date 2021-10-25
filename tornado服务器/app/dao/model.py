from sqlalchemy.ext.declarative import declarative_base   #数据库建模
from sqlalchemy import Column,VARCHAR,INTEGER,Date
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:xingzhu2046@localhost:3306/cov?charset=utf8")
Base = declarative_base()

class Province(Base):
    __tablename__ = 'province'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    地区 =Column(VARCHAR(30))
    新增病例 = Column(INTEGER)
    现有病例 = Column(INTEGER)
    累计病例 = Column(INTEGER)
    死亡 = Column(INTEGER)
    治愈 = Column(INTEGER)
    更新日期 = Column(Date)

if __name__ == '__main__':
    #创建表格
    Base.metadata.create_all(engine)
