from app.views.indexHander import IndexHander
from app.views.homeHander import HomeHander, UpdateHander

urls = [
            (r'/',IndexHander),
            (r'/home', HomeHander),
            (r'/update',UpdateHander)
        ]