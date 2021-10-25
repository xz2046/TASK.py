from pyecharts import options as opts
from pyecharts.charts import Map

from app.dao.datascorce import Datascorce

#从Datascor中导入数据，开始作图

pieces = [             #制作图例索引
    {'value':0, 'color':'#F5F5F5'},
    {'min':1, 'max':9},
    {'min':10, 'max':99},
    {'min':100, 'max':499},
    {'min':500, 'max':999},
    {'min':1000, 'max':9999},
    {'min':10000, 'lable':'1000人及以上'}
]
class ProvinceMap():   
    def __init__(self):
        ds = Datascorce()
        self.c = (
            Map(init_opts=opts.InitOpts(width='790px', chart_id='china_map'))                                                                           #图例颜色
            .add("新增病例", [list(z) for z in zip(ds.df['地区'], ds.df['新增病例'])], "china", itemstyle_opts=opts.ItemStyleOpts(color='#DAA520'))
            .add("现有病例", [list(z) for z in zip(ds.df['地区'], ds.df['现有病例'])], "china", itemstyle_opts=opts.ItemStyleOpts(color='#2F4F4F'))
            .add("累计病例", [list(z) for z in zip(ds.df['地区'], ds.df['累计病例'])], "china", itemstyle_opts=opts.ItemStyleOpts(color='#00008B'))
            .add("治愈人数", [list(z) for z in zip(ds.df['地区'], ds.df['治愈'])], "china", itemstyle_opts=opts.ItemStyleOpts(color='#228B22'))
            .add("死亡人数", [list(z) for z in zip(ds.df['地区'], ds.df['死亡'])], "china", itemstyle_opts=opts.ItemStyleOpts(color='	#696969'))
            .set_global_opts(
                legend_opts=opts.LegendOpts(selected_mode='single'),
                visualmap_opts=opts.VisualMapOpts(max_=70000,is_piecewise=True,pieces=pieces),
            ))
    def get_html(self):
        return self.c.render_embed()       #返回html代码
