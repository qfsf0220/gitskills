import json
import urllib.parse
from hashlib import md5
import re
from multiprocessing.pool import Pool

from requests.exceptions import  RequestException

import  requests
headers = {
"authority":"www.toutiao.com",
"method":"GET",
"path":"/a6525632340415218190/",
"scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
"cache-control":"max-age=0",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

def get_search_page(offset,keywd):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keywd,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    'from':'search_tab'
    }

    url='https://www.toutiao.com/search_content/?' +urllib.parse.urlencode(data)
    print(url)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return (response.text)
        else:
            return None
    except RequestException:
        print("请求索引页出错")
        return None
def parse_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for i in data.get("data"):
            yield i.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return (response.text)
        else:
            return None
    except RequestException:
        print("请求内容详细页出错",url)
        return None

def paser_detail_page(html):
    a=re.findall(r"content: '(.*?);',",html,re.S)
    for i in a :
        b=re.findall(r"x3D;&quot;(.*?)&quot",i)
        blist = [x for x in filter(lambda x: x.isdigit() == False , list(set(b)))]
        for i in blist:
            if not i.startswith("http"):
                print(i)
        for i in blist:
            if i.startswith("http"):
                download_image(i)

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            save_image(response.content) #字节形式
            print("下载中：",url,"")
        return None
    except RequestException:
        print("请求图片链接出错",url)
        return None
def save_image(content):
    file_path= "E://pic/" +md5(content).hexdigest()+".jpg"
    with open(file_path,'wb') as f:
        f.write(content)
        f.close()

def main(offset):
    html= get_search_page(offset,"街拍")
    for i in parse_page(html):
        if i == None:
            pass
        else:
            html=get_page_detail(i)
            paser_detail_page(html)

if __name__ == '__main__':
    pool =Pool()
    pool.map(main,range(0,101,20))