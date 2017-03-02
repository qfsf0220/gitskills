# -*- coding: utf-8 -*-
import time,threading
import sys,urllib
from pyquery import PyQuery as pq


def get_html():
    x=[]
    a=range(2,18)
    a.insert(0,'index')
    for i in a:
        url='http://www.pythontab.com/html/pythonhexinbiancheng/%s.html' % i
        # print url
        c=urllib.urlopen(url)
        filec=c.read()
        p=pq(filec)
        for i in range(10):
            a=p('li').find('h2').eq(i).html()
            x.append(a)

    f=open('d:/pythontab.txt','w+')
    for i in x:
        if i != None:
            print i

            f.write(i.encode('gbk','ignore')+'\n')
    f.close()


def loop():
    print("thread %s is " % threading.current_thread().name)
    for i in range(5):
        print ("thread %s,%s" %(threading.current_thread().name,i))
    print ("thread %s end")% threading.current_thread().name

print("thread %s is ") %threading.current_thread().name
t=threading.Thread(target=get_html())
t.start()
t.join()

# print("thread %s end")%threading.current_thread().name
#
# get_html()






# import threading,time
#
# exitFlag=0
#
# class myThread(threading.Thread):
#     def __init__(self,threadID,name,counter):
#         threading.Thread.__init__(self)
#         self.threadID=threadID
#         self.name=name
#         self.counter=counter
#     def run(self):
#         print "starting"+self.name
#         print_time(self.name,self.counter,5)
#         print "exiting"+self.name
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             thread.exit()
#         time.sleep(delay)
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#         counter -= 1
#
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
#
#
# print ("done")
























