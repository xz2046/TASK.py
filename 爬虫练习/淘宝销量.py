import requests


def open_url(name):
    handers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    url = "https://s.taobao.com/search"
    params = {"ie": "utf8","sourceId": "tb.index","search_type": "item","commend": "all","q": name}
    res = requests.post(url, params=params)
    return res


def main():
    name = input("请输入想查询关键字：")
    res = open_url(name)

    with open("res.txt", "w", encoding="utf-8") as f:
        f.write(res.text)


if __name__ == "__main__":
    main()
