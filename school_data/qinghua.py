import requests
import bs4
import pandas as pd

def open_url(i):
    url = 'http://www.civil.tsinghua.edu.cn/he/essay/340/{}.html'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    return res

def find_res(res):
    content = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    targest = soup.find('div', class_="content")
    targest1 = soup.find('div', class_="name")
    targest2 = soup.find('div', class_="msg")
    content.append(targest1.text)
    content.append(targest2.text)
    content.append(targest.text)
    return content

def with_content(content):
    name = ['姓名', '联系方式', '资料']
    df = pd.DataFrame(columns=name, data=content)
    print(df)
    df.to_csv('./qinghuajianzhuxueyuan.csv', mode='a' ,encoding='utf8')


def main():
    content_all = []
    #for i in range(1000,2500):
    try:
        res = open_url(611)
        content = find_res(res)
        content_all.append(content)
        print()
    except:
        pass
    #with_content(content_all)

if __name__ == '__main__':
    main()
