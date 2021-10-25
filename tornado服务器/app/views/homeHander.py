from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
import json

from app.chart.charts import ProvinceMap
from app.dao.datascorce import Datascorce

class HomeHander(RequestHandler):
    def get(self):
        #self.write('这是首页')
        map = ProvinceMap()        
        html = map.get_html()       #获取charts中制作的地图html代码
        self.render('index.html', x = {'html': html})           #将html代码发送到index页面嵌入


users = set()
class UpdateHander(WebSocketHandler):   #WebSocket继承WebSocketHandler
    '''def get(self):                   #轮询版继承RequestHandler
        ds = Datascorce()
        values = ds.get_values()
        self.write(json.dumps(values))'''

    def open(self):
        #当接受到客户端的请求时，自动调用。
        #print('成功接受请求')
        #只要接受到客户端请求，就把用户的webscoket添加到users里面
        users.add(self)

    def on_message(self, message):
        #当接受到客户端的数据时，自动调用。
        #只要有客户端给服务器发信息，就全网广播最新数据
        print(f'{message}')
        for user in users:
            ds = Datascorce()
            values = ds.get_values()
            user.write_message(json.dumps(values))

    def on_close(self):
        users.discard(self)