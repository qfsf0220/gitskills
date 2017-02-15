#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import urllib.request
import urllib.parse
import string
from pyquery import PyQuery as pq
from queue import Queue
import threading

q=Queue()
b=[]
a=['徐汇臻园','东湾度假村','苑宏新村','中海瀛台','徐汇苑','南方新村','盛华景苑','徐汇华园','紫阳花园','印象欧洲','浦润苑','华唐苑','银泰苑','新凯家园一期','中冶锦城','漓江山水花园','华泾绿苑','华泾五村','华欣家园','东湾小区','馨宁公寓','徐汇新干线','爱庐世纪新苑','新弘国际城','南方城','晶欣坊','华发小区','枫桦景苑','华建一街坊','华沁家园','长桥一村','长桥五村']

ab=['南方新村','盛华景苑','徐汇华园','枫桦景苑']

from multiprocessing import Pool

def test(i):
    url3='http://sh.lianjia.com/ershoufang/rs%s' % i
    url4=urllib.parse.quote(url3,safe=string.printable)
    webpage2=urllib.request.urlopen(url4)
    data2=webpage2.read()
    d2=pq(data2)
#    print  (d2('.wrapper').find('.botline').eq(0).text())
    url='http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=%s' % i
    url2=urllib.parse.quote(url,safe=string.printable)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url2).read()
    data=data.decode('utf-8')
    d=pq(data)
#    print (d('.comm-price').text())
    x=[d('.comm-price').text() , d2('.wrapper').find('.botline').eq(0).text() ]
    q.put(x)


if __name__ == '__main__':
    result=list()
    for i in a:
        t1=threading.Thread(target=test,args=(i,))
        t1.start()
        t1.join()
        while not q.empty():
            result.append(q.get())
    for item in result:
        print(item)
