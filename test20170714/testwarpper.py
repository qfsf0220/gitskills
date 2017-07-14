import datetime
import time

# def  now():
#     '''
#     ---
#     this is a wrapper test
#     ---
#     '''
#     print(datetime.datetime.now())
#
# def log(aa):
#     def wrapper(*aaa,**a):
#         print('这个函数返回了 %s' % aa())
#         return aa(*aaa,**a)
#     return wrapper
#
# @log
# def now():
#     return  "1234"
#
# now()
#
#
# def ppp(*aaa,**a):
#     print(aaa)
#     for i in aaa:
#
#         print(i)
#
#
# def person( **kw):
#     print( 'other:', kw)
#
# person(a=22,b='cc',d=1234)
#
# def aaa(aa):
#     def wrapper():
#         a=time.time()
#         aa()
#         b=time.time()
#         print("用了："+str(b-a)+"秒。")
#         return aa.__name__
#
#     return wrapper
#
# @aaa
# def titttime():
#     time.sleep(2)
#     print("done0")
#
#
# print(titttime())
#

def tt(aa):
    def wrapper(name):
        '''
123412341234
        '''
        a=time.time()
        aa()
        b=time.time()

        print('hi:'+name+','+'the function <'+aa.__name__+'> cost'+str(b-a)+'seconds')
        return wrapper.__doc__
    return wrapper
@tt
def xyx():
    time.sleep(2)
    print('done')

xyx('qf')
print(xyx('qf'))