import numpy as np
import pandas as pd
import os
import requests
import bs4


# 生成网页链接
def open_url(M):
    url = 'http://m.apporid.com/xian/{}yue.html'.format(M)
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                         '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ',
               }
    res = requests.get(url, headers=headers)
    return res


# 查找网页数据
def deal_res(res):
    temperature = []

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    targets = soup.find("ul", class_="tqullist tqicon28x20")
    targets = targets.find_all('li')
    for each in targets:
        temperature.append(each.text.split())  # 按空格分割日期和其他资料

    t2 = []  # 提取其他天气资料部分
    for i in temperature:
        t2.append(i[1])
    return t2, temperature


# 处理天气数据，转为dataframe，并保存为excel
def deal_temperature(temperature, tempMin, tempMax, Weather, M):
    wmin = []
    wmax = []
    for i in tempMin:
        wmin.append(i.replace("℃", ""))  # 去除“℃”符号
    for i in tempMax:
        wmax.append(i.replace("℃", ""))

    t1 = np.array(temperature).reshape(len(temperature), 2)
    df = pd.DataFrame(t1, columns=["日期", "b"])
    df['天气'] = pd.DataFrame(Weather)
    df['最高温度'] = pd.DataFrame(wmax)
    df['最低温度'] = pd.DataFrame(wmin)
    del df['b']
    df.to_excel(r'E:\Python Pycharm\练习\fenxi\tianqi\{}weather.xlsx'.format(M))


# 读取天气数据，并合并，提取需要部分
def deal_weather():
    excels = [pd.read_excel(fname) for fname in os.listdir('./') if 'xls' in fname]
    df = pd.concat(excels)
    df['日期'] = pd.to_datetime(df["日期"])
    df = df.set_index('日期', drop=True)
    df = df[['天气', '最高温度', '最低温度']]
    return df


# 读取营业数据，提取需求部分
def open_file():
    excels = [pd.read_excel(fname) for fname in os.listdir('./') if 'xls' in fname]
    df = pd.concat(excels)
    df.to_excel(r'E:\Python Pycharm\练习\fenxi\huizong.xlsx')
    pd.set_option('display.max_rows', None)
    df = pd.read_excel(r'E:\Python Pycharm\练习\fenxi\huizong.xlsx', header=2)
    df = df[['日期', '订单笔数', '营业收入']]
    df = df[pd.notnull(df['日期'])]
    df = df[~df['日期'].isin(['日期'])]
    df["日期"] = pd.to_datetime(df["日期"])
    df = df.set_index('日期', drop=True)
    return df


# 判断是否为中文
def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# 将天气资料部分切割为天气，最高温度，最低温度
def group_weather(t2):
    Weather = []
    tempMax = []
    tempMin = []
    for each in t2:
        index = 0
        for char in each:
            if not isChinese(char):
                weather = each[0:index]
                temps = each[index:].split("/")
                tempmin = temps[0]
                tempmax = temps[1]
                Weather.append(weather)
                tempMin.append(tempmin)
                tempMax.append(tempmax)
                break
            else:
                index += 1
    return Weather, tempMax, tempMin


def main():
    os.chdir(r'E:\Python Pycharm\练习\fenxi\1—7')  # 更改工作目录
    df = open_file()
    for M in range(1, 8):  # 循环爬取不同月份天气数据
        res = open_url(M)
        t2, temperature = deal_res(res)
        Weather, tempMax, tempMin = group_weather(t2)
        deal_temperature(temperature, tempMin, tempMax, Weather, M)
    os.chdir(r'E:\Python Pycharm\练习\fenxi\tianqi')  # 更改工作目录，读取销售数据
    df1 = deal_weather()
    df2 = df.join(df1, how="outer")  # 合并两个dataframe
    df2 = df2.reset_index()
    df2['week'] = df2["日期"].dt.dayofweek + 1  # 根据时间序列生成周几数据
    df2 = df2.set_index("日期", drop=True)
    df2.to_excel(r"E:\Python Pycharm\练习\fenxi\collect.xlsx")  # 保存全部数据


if __name__ == '__main__':
    main()
