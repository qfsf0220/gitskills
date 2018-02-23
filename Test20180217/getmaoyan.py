from multiprocessing.pool import Pool

import requests
import json,re
def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return  response.text
    else:
        return None
def parse_one_page(html):
    a=re.findall("<i class=\"board-index.*?>(\d+)</i>.*?title=\"(.*?)\" class.*?star\">(.*?)</p>.*?releasetime\">(.*?)</p>.*?integer\">(.*?)</i>.*?fraction\">(.*?)</i>",html,re.S)
    for i in a :
        yield {'排名':i[0],'片名':i[1],
           '主演':i[2].strip().split('：')[1],
               "上映时间":i[3].split('：')[1],
               "评分":str(i[4])+str(i[5])}
def writefile(content):
    with open ('filmscore.txt','a',encoding="utf-8") as f: #utf8打开
        f.write(json.dumps(content,ensure_ascii=False)  + "\n") #json.dumps() 把字典转换为string 取消ascii编码
        f.close()
def main(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for i in parse_one_page(html):
        print(i)
        writefile(i)
if __name__ == '__main__':
    pool =Pool()
    pool.map(main,[x for x in range(0,101,10)])



