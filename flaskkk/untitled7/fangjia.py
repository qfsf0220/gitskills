#-*- encoding:utf-8 -*-
import urllib.request
import urllib.parse
import string
import scrapy

a=['南方新村','盛华景苑','徐汇华园']
for i in a:
    url='http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=%s' % i
    url2=urllib.parse.quote(url,safe=string.printable)

    webpage=urllib.request.urlopen(url2)
    data=webpage.read()
    data=data.decode('utf-8')
    print(data)