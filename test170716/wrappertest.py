__author__ = 'qfsf'
import time
# def a(b):
#     def wrapper(firstname,lastname):
#         time1=time.time()
#         b()
#         time2=time.time()
#         print('hi '+firstname+lastname+',cost '+str(int(time2-time1))+' seconds')
#         print(b.__name__)
#         print(a.__name__)
#
#     return wrapper
#
# @a
# def aabc():
#     time.sleep(3)
#     print('Done')
# print(aabc('qf','sf'))

#
# def a(func):
#     def wrapper(*a,**aa):
#         x=func(*a,**aa)
#         return x
#     return wrapper
#
# @a
# def myfunc(a,b,c,d):
#     return (a+b+c+d)
# @a
# def myfunc2(a,b):
#     return (a-b)
# print(  myfunc2(5,4) )
# myfunc(1,2,3,4)
# addresult=myfunc(2,3,4,5)
# print(addresult)

# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, arg))
#             func()
#             print("  after %s called [%s]." % (func.__name__, arg))
#         return __deco
#     return _deco
# @deco("mymodule")
# def myfunc():
#     print(" myfunc() called.")
# @deco("module2")
# def myfunc2():
#     print(" myfunc2() called.")
# myfunc();myfunc2()
# def x(arg):
#     def y(func):
#         def wrapper():
#             print("the wrapper\'s args is: %s" % arg)
#             func()
#             print('the func name  %s' % func.__name__)
#         return wrapper
#     return y
# @x('abc')
# def my1():
#     print('this is my1 func..')
# my1()

def a(arg):
    if arg==1:
        def b(func):
            def wrapper():
                print('args='+str(arg))
                func()
                print("func-->end")
            return wrapper
        return b
    else:
        def b(func):
            def wrapper():
                func()
            return wrapper
        return b

@a(1)
def myfunc():
    print('ok')
myfunc()