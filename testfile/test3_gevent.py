#!/usr/bin/env python
#-*- coding:utf-8 -*-
from  multiprocessing import Process
import gevent,requests
from gevent import monkey
monkey.patch_all()

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
def fetch(url):
    try:
        s=requests.Session()
        r=s.get(url,headers=headers)
    except Exception as e :
        print(e)
    return ""

def process_start(tasks):
    gevent.joinall(tasks)

def task_start():
    task_list=[]
    xiaoquming = ['中海瀛台', '徐汇臻园', '徐汇华园', '枫桦景苑']
    sourceurl = "http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw="
    realurl =[ sourceurl+x for x in xiaoquming]
    print(realurl)

    for url in realurl:

        task_list.append(gevent.spawn(fetch,url))

        p = Process(target=process_start,args=(task_list,))

        p.start()

if __name__ == '__main__':
    task_start()