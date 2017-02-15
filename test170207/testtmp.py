#-*- coding:utf-8 -*-
__author__ = 'qfsf'
import urllib
import string
import urllib.parse
import urllib.request
from pyquery import PyQuery as pq


url='http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=盛华景苑'

url2=urllib.parse.quote(url,safe=string.printable)
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url2).read()
d=pq(data)
xx=[]
xx.append(d('.comm-price').text())
print(xx)