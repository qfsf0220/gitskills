# -*- coding:utf8 -*-
# from gevent.server import   StreamServer
#
# def conn_handler(socket,address):
#     for l in socket.makefile('r'):
#         socket.sendall(l)
#
# if __name__ == '__main__':
#     server = StreamServer(('0.0.0.0',8000),conn_handler)
#     server.serve_forever()
import urllib.request
from gevent import  monkey
monkey.patch_all()

import  urllib
from gevent.pool import Pool

def download(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

def f(url):
    print("get :%s"% url)
    data = urllib.request.urlopen(url).read().decode("utf-8")



if __name__=='__main__':
    urls = ["http://www.qfsf0220.top"]*50
    pool = Pool(10)
    print(pool.map(download,urls))

