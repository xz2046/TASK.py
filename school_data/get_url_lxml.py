import requests
from lxml import etree

def open_url():
    url = 'http://www.sppm.tsinghua.edu.cn/szdw/qzjs/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    res.encoding="utf-8"
    res=res.text
    return res

def etree_res(res):

    res_xpath = etree.HTML(res)
 
    for i in res_xpath.xpath('//div[@id="xp_zw"]'):
        s = i.xpath('.//a/@href')
        urls = s[26:]

    return urls

def all_url(urls):

    all_urls = []
    for i in urls:
        str1 = 'http://www.sppm.tsinghua.edu.cn' + i
        all_urls.append(str1)
    return all_urls

def main():
    res = open_url()
    urls = etree_res(res)
    all_urls = all_url(urls)
    return all_urls

#main()
