import pandas as pd
import requests
import bs4 
import get_url_bs4

def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    return res


def find_res(res):
    content = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    all = soup.get_text()
    all = all.replace("\n", "")
    all = all.replace("\t", "")
    content.append(all)
    return content

def with_content(content):
    name = ['资料']
    df = pd.DataFrame(columns=name, data=content)
    print(df)
    df.to_csv('./jingjiguanli.csv', mode='a' ,encoding='utf8')

def main():
    urls = get_url_bs4.main()
    print(urls)
    for url in urls:
        res = open_url(url)
        content = find_res(res)
        with_content(content)

if __name__ == "__main__":
    main()
