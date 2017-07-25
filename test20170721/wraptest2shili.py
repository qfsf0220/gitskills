from wraptest20725 import *

class c3:
    @abc(c1)
    def myfunc1(self):
        print('myfunc1111111')

    @abc(c1)
    @abc(c2)
    def myfunc2(self):
        print('myfunc222222222')


if __name__ == '__main__':
    a= c3()
    a.myfunc1()
    print("----"*10)
    a.myfunc2()