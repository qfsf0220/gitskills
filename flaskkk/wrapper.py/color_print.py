# -*- coding:utf-8 -*-
import time,sys
# def color_print(msg, color='red', exits=False):
#
#     color_msg = {'blue': '\033[1;46m%s\033[0m',
#                  'green': '\033[1;42m%s\033[0m',
#                  'yellow': '\033[1;43m%s\033[0m',
#                  'red': '\033[1;41m%s\033[0m',
#                  'title': '\033[30;42m%s\033[0m',
#                  'info': '\033[32m%s\033[0m'}
#     xxx = color_msg.get(color, 'red') % msg
#     print xxx
#     # if exits:
#     #     time.sleep(2)
#     #     sys.exit()
#     # return msg
# color_print('这个是test','yellow')

def aa(func):
    def wrapper(a,b):
        colorlist = {'blue': '\033[1;36m%s\033[0m',
                         'green': '\033[1;32m%s\033[0m',
                         'yellow': '\033[1;33m%s\033[0m',
                         'red': '\033[1;31m%s\033[0m',
                         'title': '\033[1;4;5;30;32m%s\033[0m',
                         'info': '\033[32m%s\033[0m'}
        print colorlist.get(b) % '*'*10
        print colorlist.get(b) % a
        print colorlist.get(b) % '*'*10

    return wrapper

@aa
def pprint(a,b):
    print(a,b)


pprint("弄好啊。。boss",'title')



def aa(arg,*args,**kwargs):
    print arg
    for i in args:
        print i
    for x,y in kwargs.items():
        print x,y



