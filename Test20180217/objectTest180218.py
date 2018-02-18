#-*- coding:utf-8 -*-
import logging as l

l.basicConfig(level=l.DEBUG,format='%(asctime)s\t%(levelname)s\t%(message)s')
class test:
    pass


l.debug(test.__class__.__base__)#这里显示是 基类 object

#test1
class test1:
    def test1(self):
        return (self.a+self.b)

t1 = test1()
t1.a,t1.b=5,6  #延迟赋值 一般不使用
l.debug(t1.test1())

class test2:
    def test2(self,a,b):
        self.a= a
        self.b = b
        return self.a+self.b
t2= test2()

l.info(t2.test2(5,6))
x = [t2.test2(x+1,y) for x in range(3) for y in (2,4,8,10,22)]
l.info(x)

class test3:
    def __init__(self,a,*b):
        self.a=a
        self.bs=list(b)
        print(self.a)
        print(self.bs)

    def get11(self):
       print(sum(x for x in self.bs))

t3 = test3(1,2,3,4)
t3.get11()

class test4(test3):
    def __init__(self,abc):
        super().__init__(1,2,3)
        self.abc= abc
t4 = test4(878)

print(t4.bs,t4.abc)
