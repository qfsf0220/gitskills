# -*- coding:utf8 -*-
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s:' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print ("xxxxxxxxxxxxxxxxxxxxx")
#
# f=now
#
# f()
#
# print now.__name__
#
# print f.__name__

# def log(aa):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print ('%s,%s():' % (aa,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
# @log("nonghao")
# def now():
#     print('xxxxxxxxxxxxx')
#
# now()


import functools

# def log(func):
#     # @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print ('before %s:'% func.__name__)
#         a= func(*args,**kw)
#         print ('after %s:'% func.__name__)
#         return a
#     return wrapper
#
# @log
# def hi():
#     print("hihihi")
#
# hi()

###########################
# import logging,time
# def aaaa(text):
#     def uselogging(func):
#         def wrapper(*args,**kw):
#             print ("start %s,%s" % (text,func.__name__))
#             print 1
#             logging.warn("-%s-,%s is running"% (text,func.__name__))
#             time1 = time.time()
#             a=func(*args, **kw)  #这个运行hi()函数
#             time2=time.time()
#             print 3
#             print"usetime" ,time2-time1
#             print ("end %s,%s" % (text,func.__name__))
#             return a
#         return wrapper
#     return uselogging
#
# @aaaa("hi,qf")
# def hi():
#     print("2")
#     time.sleep(2)
#
# if __name__=='__main__':
#     print __name__
#     hi()
#
# import os
#
#
# os.path.exists()
from collections import Iterable
print isinstance('abc',Iterable)

print  [x*2 for x in range(1,60) if x%2==0]

print [a+b for a in ['aa','bb','cc'] for b in ('dd','ee','ff')]

d={'x':'A','y':'B','z':'C'}
for i in [k+' = '+v for k,v in d.items()]:
    print i
for k,v in d.items():
    print k,'=',v


kk=['NA',"NBADF","QfSf"]
print [s.lower() for s in kk]


L=['HeLLo', 'WorlD', 18, 'Apple', None]
for i in L:
    if isinstance(i,str) == False:
        L.remove(i)
print [x.lower() for x in L]

from collections import Iterable
gg=[1,2,3,4]
print isinstance(gg,Iterable)
print isinstance('abc',Iterable)
J=['HeLLo', 'WorlD', 18, 'Apple', None]

print [ x.upper() for x in J if isinstance(x,str)]


from collections import Iterator
def aaa():
    yield (1)
    yield (2)
    print isinstance([1,2,3,4,5],Iterator)
    print isinstance(iter([1,2,3,4,5,6]),Iterator)
    a=iter([1,2,3,4,5,6])
    while 1:
        print a.next()



a=aaa()
print type(aaa())
while 1: print a.next()

fx=[1,2,3,4,5]
print fx.next()
print fx[2]

import json.tool

json.tool.main()