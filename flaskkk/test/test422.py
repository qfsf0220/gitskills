#__auther__='feng.qian'
# -*- coding: utf-8 -*-
import  json
#
# from bs4 import BeautifulSoup as bs
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# sss = bs(html_doc,"lxml")
# print sss.prettify()
# print "*"*10
#
# print sss.title.string
#
# print sss.find_all(a)









# b=[x for x in range(2,30) if x%2==0]
# print b
#
# c=iter(b)
# while 1:
#     print c.next()


#
# def aaa(a):
#     def bbb(b):
#         print a+b
#     return bbb(2)
# aaa(1)
############################


# def outer(a):
#     def iner(b):
#         print '%s,%s' % (a('hello'),b)
#     return iner
#
# @outer
#
# # shuchu = outer(shuchu())
#
# def shuchu(x):
#     print shuchu.__name__
#     return x
#
# shuchu("world")


# def loginok(func):
#     print "我是小钱"
#     def aaa(a):
#         return  func(a)
#     return  aaa
#
# @loginok
# def sayhi(name):
#     print "%s好啊" % name
#
#
# sayhi("各位老总")
#
#
# def a(x):
#     print x
#
# def geta(func,g):
#     print func(g)
#
# geta(a,"nihao")

import time
# def get_time():
#     time.sleep(3)
#     print "over"
#
# get_time()


#
# def outer(func):
#     def wrapper():
#         starttime = time.time()
#         func()
#         endtime=time.time()
#         print "used",endtime-starttime
#     return wrapper
#
# @outer
# def get_timeee():
#     time.sleep(3)
#     print "over"
#
# get_timeee()
#
# def a(x):
#     return x
#
# def ab(func):
#     def wrapper(c):
#         return func(c)
#     return wrapper
#
# a=ab(a)
# a()

# def deco(F):
#     def newf(a,b):
#         starttime = time.time()
#         print "you inputed  %s and %s ,it will be wait %s second and print this <%s> " % (a,b,a,b)
#         F(a,b)
#         endtime=time.time()
#         print 'used:',endtime-starttime
#     return  newf
# @deco     #1
# def add(a,b): #3
#     print b
#     time.sleep(a)
# @deco     #2
# def jian(a,b):
#     print int(a)-int(b)
#     time.sleep(a)
#
# add(2,3)
# jian(2,4)
# #装饰器的意义在于 调用函数来修饰函数，提高复用性 如#1 #2
# # addshilihua=deco(add) #这里，装饰器@deco 其实就是等于  吧#3的add函数作为参数代入到deco函数,addshilihua
# # addshilihua(3,4)      #把deco函数实例化 等于add函数代入实参（3,4）并同时使用了deco（）
#
import urllib2,cookielib
url = "http://www.baid.com"

cj=cookielib.CookieJar()   #创建cookie的容器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  #创建opener
urllib2.install_opener(opener=opener)#urllib安装了上面的iopener以后拥有了处理cookie的能力
response3=urllib2.urlopen(url)#
print response3.getcode()#
print cj
print response3.read()