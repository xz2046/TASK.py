import requests
from lxml import etree
import pandas as pd
import get_url_bs4
import get_url_lxml

def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    res.encoding="utf-8"
    res=res.text
    return res

def etree_url(res):
    # print(res) 检查解码是否正确
    contents = []
    res_xpath = etree.HTML(res)   #//*[@id="vsb_content"]/div/table/tbody/tr[1]/td[2]/span
    name0 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[1]/td[2]/text()') 
                            #//div[@id="vsb_content"]/div/div/table/tbody/tr[1]/td[2]
    name1 = res_xpath.xpath('//div[@id="vsb_content_100"]/div/table/tbody/tr[1]/td[2]/text()')
    name2 = res_xpath.xpath('//div[@id="vsb_content"]/div/div/div/table/tbody/tr[1]/td[2]/text()')
    title0 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[3]/td[2]/text()')
    title1 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[3]/td[2]/span/text()') 
    title2 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[3]/td[2]/p/text()')
    content0 = res_xpath.xpath('//div[@id="vsb_content"]/div/p/text()')
    content1 = res_xpath.xpath('//div[@id="vsb_content"]/div/p/span/text()') 
    msg0 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[5]/td[2]/text()')
    msg1 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[5]/td[2]/a/text()')
    msg2 = res_xpath.xpath('//div[@id="vsb_content"]/div/table/tbody/tr[5]/td[2]/p/text()') 
    msg = msg0 + msg1 + msg2 
    title = title0 + title1 +title2
    content = content0 + content1
    name = name1 + name0 +name2
    contents.append([name, title, msg, content])  
    print(name,title,msg,content)
    return contents

def with_content(content):
    df = pd.DataFrame(data=content)
    print(df)
    df.to_csv('./school_data/data/环境学院.csv', mode="a" ,encoding='utf8')

def main():
    url = ['https://www.env.tsinghua.edu.cn/info/1140/5366.htm','https://www.env.tsinghua.edu.cn/info/1149/6046.htm','https://www.env.tsinghua.edu.cn/info/1149/5964.htm']
    for i in url:
        try:
            res = open_url(i)
            content = etree_url(res)
            #with_content(content)
        except:
            pass

if __name__ == '__main__':
    main()