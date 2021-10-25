import requests
import bs4

def get_url():
    urls = ['https://www.smarx.tsinghua.edu.cn/szqk/js.htm', 'https://www.smarx.tsinghua.edu.cn/szqk/spjs_jzjs.htm', 'https://www.smarx.tsinghua.edu.cn/szqk/fjs.htm', 'https://www.smarx.tsinghua.edu.cn/szqk/js1.htm','https://www.smarx.tsinghua.edu.cn/szqk/bsh.htm']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }

    for url in urls:
        print(url)
        res = requests.get(url, headers=headers)
    return res

def find_url(res):
    urla = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser') 
    url1 = soup.find("span", class_="p_pages")
    u = url1.find_all("a")
    for url in u:
        url = url.get("href")
        url = url.replace("../", "")
        #print(type(url))
        print(url)
        urla.append(url)
    return urla

def open_url():
    url = 'https://www.smarx.tsinghua.edu.cn/szqk/js.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    print(res)
    return res

def find_res(res):
    content = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser') 
    urls = soup.find("ul", class_="teach-list clearfix")
    a = urls.find_all("a")
    for i in a:
        url = i.get("href")
        url = url.replace("../", "")
        #print(type(url))
        print(url)
        url = 'https://www.env.tsinghua.edu.cn/' + url
        content.append(url)
    return content

def main():
    res = get_url()
    urla = find_url(res)
    print(urla)
    #res = open_url()
    #urls = find_res(res)
    # print(urls)
    

if __name__ == '__main__':
    main()