import requests
import bs4
import openpyxl
import re


def open_url(url):
    header = {
        "User-Anget": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.212 Mobile Safari/537.36"}
    res = requests.get(url, headers=header)
    return res


def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    table = soup.find_all("table", border="1")
    target = iter(table)
    for each in target:
        '''
        if each.text.isnumeric():
            data.append([
                re.search(r'\w?',next(target).text).group(1),
                re.search(r'^\w?', next(target).text).group(2)
            ])
            '''
        print(each.text)

    return data


def to_excel(table):
    pass


def main():
    url = "https://edu.sina.cn/gaokao/bkzn/2020-05-15/detail-iircuyvi3207918.d.html?from=wap"
    res = open_url(url)
    find_data(res)


if __name__ == "__main__":
    main()
