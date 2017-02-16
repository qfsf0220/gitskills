#-*- coding:utf-8 -*-
import string
import urllib.parse
import urllib.request
import urllib, re, string
import threading, queue, time
from pyquery import PyQuery as pq
import sys

a=['中海瀛台','徐汇臻园','徐汇华园','枫桦景苑']


_DATA = []
FILE_LOCK = threading.Lock()
SHARE_Q = queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 3  #设置线程的个数

class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()  #调用父类的构造函数
        self.func = func  #传入线程函数逻辑

    def run(self) :
        self.func()

def worker() :
    global SHARE_Q
    while not SHARE_Q.empty():
        url = SHARE_Q.get() #获得任务
        my_page = get_page(url)
        # find_title(my_page)  #获得当前页面的电影名
        #write_into_file(temp_data)
        time.sleep(1)
        SHARE_Q.task_done()

def get_page(url):
    # url='http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=盛华景苑'

    url2=urllib.parse.quote(url,safe=string.printable)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url2).read()
    return data

# def get_price(data):
#     temp_data = []
#     d=pq(data)
#     item= d('.comm-price').text()
#     _DATA.append()

def main():
    global SHARE_Q
    threads =[]
    url = "http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw={name}"
    for i in a:
        SHARE_Q.put(url.format(name=i))
    for i in range(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    SHARE_Q.join()
    for i in _DATA:
        for j in i:
            print(j)


if __name__=="__main__":
    main()