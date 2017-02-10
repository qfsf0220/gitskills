#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import urllib.request
import urllib.parse
import string
#import scrapy
from pyquery import PyQuery as pq
import re

b=[]
ab=['徐汇臻园','东湾度假村','苑宏新村','中海瀛台','徐汇苑','南方新村','盛华景苑','徐汇华园','紫阳花园','印象欧洲','浦润苑','华唐苑','银泰苑','新凯家园一期','中冶锦城']
a=['南方新村','华泾五村','徐汇华园']
for i in a:
    url='http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=%s' % i #安居客
    url2=urllib.parse.quote(url,safe=string.printable)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url2).read()
    #url3='http://www.dooioo.com/ershoufang/rs%s' % i #链家
    url3='http://sh.lianjia.com/ershoufang/rs%s' % i #链家
    url4=urllib.parse.quote(url3,safe=string.printable)

    #webpage=urllib.request.urlopen(url2)
    #data=webpage.read()
    data=data.decode('utf-8')
    #print(data)
    webpage2=urllib.request.urlopen(url4)
    data2=webpage2.read()
    #data2=data.decode('utf-8')

    d=pq(data)
    d2=pq(data2)
   #print(d('span').text()+'|'+d('em').filter('.price').text()+'|'+d('em').filter('.up').text())


    b.append([d('.comm-price').text(),d2('.wrapper').find('.botline').eq(0).text()])
def greenprint(ssttrr):
    return ('\033[0;32;40m%s\033[0m' % ssttrr)
def redprint(ssttrr):
    return ('\033[0;31;40m%s\033[0m' % ssttrr)

def yellowprint(ssttrr):
    return ('\033[0;33;40m%s\033[0m' % ssttrr)

c=sorted(b,key=lambda x:re.sub('\D','',x[0]))

for i in c:
    if '↑' in i[0].split(' ')[5]:
        print(i[0].split(' ')[0] + " 本月" + yellowprint(i[0].split(' ')[2].split('元')[0]) + "元/平方米 , 比上月 " + redprint((i[0].split(' ')[5])))
    else:
        print(i[0].split(' ')[0] + " 本月" + yellowprint(i[0].split(' ')[2].split('元')[0]) + "元/平方米 , 比上月 " + greenprint(
            (i[0].split(' ')[5])))

# for i in c[0]:
#     print(c[1][0].split(' ')[0]+" 本月"+yellowprint(c[1][0].split(' ')[2].split('元')[0])+"元/平方米 , 比上月 "+redprint((c[0][0].split(' ')[-1])))
