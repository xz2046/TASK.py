import requests
from matplotlib import pyplot as plt, font_manager
import bs4
from xpinyin import Pinyin
from tkinter import *


# 创建网址链接
def urls():
    global dates
    p = Pinyin()
    city = e1.get()
    city = p.get_pinyin(city)  # 汉字转为拼音
    city = city.replace("-", "")
    dates = variable1.get() + variable2.get()
    url = f"https://lishi.tianqi.com/{city}/{dates}.html".format(city=city, dates=dates)
    print(url)
    return url


# 爬取网页数据
def open_url(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "sec - fetch - site": "same - origin",
        "accept - encoding": "gzip, deflate, br",
        "cache-control": "max-age=0",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://www.tianqi.com/qiwen/city-xian-3/",
        "upgrade - insecure - requests": "1",
        "cokkie": "UM_distinctid=17a7045d2b737c-09469a16397897-6373264-149c48-17a7045d2b8b9a; "
                  "Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1625381262; "
                  "CNZZDATA1275796416=1699660372-1625376765-https%253A%252F%252Fwww.google.com.hk%252F%7C1625398369; "
                  "Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1625402066",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"}
    res = requests.get(url, headers=headers)
    return res


# 数据搜索
def find_s(res):
    temperature = []

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    targets = soup.find("ul", class_="thrui")
    targets = targets.find_all("div", class_="th140")
    for each in targets:
        temperature.append(each.text)
    return temperature


# 数据分组处理
def handles_list(temperature):
    global temperature_max
    temperature_max, temperature_min = [], []
    for i in range(0, len(temperature), 4):
        temperature_max.append(temperature[i].replace("℃", ""))
        temperature_min.append(temperature[i + 1].replace("℃", ""))
    return temperature_max, temperature_min


# 制作折线图
def drawing(y_max, y_min):
    city = e1.get()
    data = dates[4] + dates[5]

    y_max = list(map(float, y_max))
    y_min = list(map(float, y_min))
    y_max = list(map(int, y_max))
    y_min = list(map(int, y_min))
    my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
    plt.figure(figsize=(20, 9), dpi=100)

    x = range(1, len(temperature_max) + 1)

    plt.plot(x, y_max, label="最高温度", color="red")
    plt.plot(x, y_min, label="最低温度", color="cyan")

    xl = [data + "月{}日".format(i) for i in x]
    plt.xticks(x, xl, fontproperties=my_font, rotation=40)
    plt.yticks(range(min(y_min + y_max), max(y_min + y_max) + 4, 2))
    plt.xlabel("时间", fontproperties=my_font)
    plt.ylabel("温度", fontproperties=my_font)
    plt.title("{city}{data}月份每日温度变化表".format(city=city, data=data), fontproperties=my_font)

    plt.legend(prop=my_font)
    plt.grid(alpha=0.8)
    # plt.savefig("./{city}{data}月份每日温度变化表.png".format(city=city, data=data))
    plt.show()


def main():
    try:
        url = urls()
        res = open_url(url)
        temperature = find_s(res)
        y_max, y_min = handles_list(temperature)
        drawing(y_max, y_min)
    except AttributeError:
        lab5.grid(row=2, column=1, columnspan=4, rowspan=2, padx=10, pady=10)


# 图形界面
root = Tk()
f1 = Frame(root).grid()
lab1 = Label(f1, text="日期:").grid(row=0, column=0)
lab2 = Label(f1, text="城市:").grid(row=1, column=0)

variable1 = StringVar()
variable2 = StringVar()
variable1.set("2021")
variable2.set("01")
w = OptionMenu(f1, variable1, "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013"). \
    grid(row=0, column=1)
lab3 = Label(f1, text="年").grid(row=0, column=2)
w2 = OptionMenu(f1, variable2, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12") \
    .grid(row=0, column=3)
lab4 = Label(f1, text="月").grid(row=0, column=4)
e1 = Entry(f1)
e1.grid(row=1, column=1, columnspan=4)

b1 = Button(f1, text="确定", width=10, command=main).grid(row=1, column=5, sticky=W, padx=10, pady=5)
lab5 = Label(f1, text="数据还没统计，等等再来吧！！！", foreground="red", font=("宋体", 10))

mainloop()
