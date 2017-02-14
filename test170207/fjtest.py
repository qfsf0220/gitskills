#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import urllib.request
import urllib.parse
import string
from pyquery import PyQuery as pq
import re

b=[]
ab=['徐汇臻园','东湾度假村','苑宏新村','中海瀛台','徐汇苑','南方新村','盛华景苑','徐汇华园','紫阳花园','印象欧洲','浦润苑','华唐苑','银泰苑','新凯家园一期','中冶锦城','漓江山水花园','华泾绿苑','华泾五村','华欣家园','东湾小区','馨宁公寓','徐汇新干线','爱庐世纪新苑','新弘国际城','南方城','晶欣坊','华发小区','枫桦景苑','华建一街坊','华沁家园','长桥一村','长桥五村']
a=['中海瀛台','徐汇臻园','徐汇华园','枫桦景苑']
for i in a:
    url='http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=%s' % i #安居客
    url2=urllib.parse.quote(url,safe=string.printable)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url2).read()

    url3='http://sh.lianjia.com/ershoufang/rs%s' % i #链家
    url4=urllib.parse.quote(url3,safe=string.printable)

    data=data.decode('utf-8')

    webpage2=urllib.request.urlopen(url4)
    data2=webpage2.read()

    d=pq(data)
    d2=pq(data2)

    b.append([d('.comm-price').text(),d2('.wrapper').find('.botline').eq(0).text()])
def greenprint(ssttrr):
    return ('\033[0;32;40m%s\033[0m' % ssttrr)
def redprint(ssttrr):
    return ('\033[0;31;40m%s\033[0m' % ssttrr)
def yellowprint(ssttrr):
    return ('\033[0;33;40m%s\033[0m' % ssttrr)

c=sorted(b,key=lambda x:re.sub('\D','',x[0]))
print (c)
d= map(lambda x:re.sub('(（(.*)\))','',x[0]),c)

e= [x for x  in d ]
print(e)

for i in e :
    if '↑' in re.split('\s+',i)[5]:
        print(re.split('\s+',i)[0]+ " 本月"+yellowprint(re.split('\s+',i)[2].split('元')[0])+"元/平方米 , 比上月 " +redprint(re.split('\s+',i)[5]))
    else:
        print(re.split('\s+', i)[0] + " 本月" + yellowprint(re.split('\s+', i)[2].split('元')[0]) + "元/平方米 , 比上月 " + greenprint(re.split('\s+', i)[5]))