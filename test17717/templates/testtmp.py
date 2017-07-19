from os import path
# basepath = path.abspath(path.dirname(__file__))
# print(__file__)
# print(path.dirname(__file__))
# print(basepath)

# def a(func):
#     def wrapper(a,b):
#         print('-'*10)
#         a=(func(a,b))
#         print('result='+str(a))
#         print('-' * 10)
#     return wrapper
#
# @a
# def add(a,b):
#     return a+b
# add(1,2)

# def a(arg):
#     if arg==1:
#         def _a(func):
#             def __a(*a,**aa):
#                 print('arg ='+str(arg)+' continue.')
#                 func(*a,**aa)
#             return __a
#         return _a
#     else:
#         def _a(func):
#             def __a(*a,**aa):
#                 answer=input ('no arg!'+'\nwould you continue?(y/n)')
#                 if answer=='y' or answer=='Y':
#                     func(*a,**aa)
#             return __a
#         return _a
#
# a_arg='qf'
# @a(a_arg)
# def funtest(a,b,c,d,e):
#     from functools import reduce
#     print(reduce(lambda x,y:str(x)+str(y) ,[a,b,c,d,e])  )
#
# funtest('asd','123',0,'xx',3214)

#
# class locker:
#     def __init__(self):
#         print('locke.__init__')
#     @staticmethod
#     def jtff():
#         print("jingtaifangfa")
#     @staticmethod
#     def nosldx():
#         print('buyongshiliduixiang')
#
# def a(arg):
#     def _a(func):
#         def __a():
#             print('arg:'+str(arg))
#             # arg.jtff()
#             func()
#             # arg.nosldx()
#         return __a
#     return _a
#
# @a(locker)
# def myfun():
#     print('123123')
#
# myfun()
class aaa:
    def __init__(self):
        print('__init__()')
    @staticmethod
    def aaa_a():
        print('aaa_a')
    @staticmethod
    def aaa_b():
        print('aaa_b')
class bbb(aaa):
    @staticmethod
    def aaa_a():
        print("bbb_a")
    @staticmethod
    def aaa_b():
        print("bbb_b")
    @staticmethod
    def bbb_a():
        print("real bbb_a")

def a(arg):
    def _a(func):
        def __a(*a,**aa):
            arg.aaa_a()
            func(*a,**aa)
            arg.aaa_b()
            # arg.bbb_a()
        return __a
    return _a






