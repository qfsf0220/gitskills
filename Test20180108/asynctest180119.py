#-*- coding:utf-8 -*-
import os
import inspect

#生成器函数
#GEN_CREATED # 等待开始执行
#GEN_RUNNING # 解释器正在执行（只有在多线程应用中才能看到这个状态）
#GEN_SUSPENDED # 在yield表达式处暂停
#GEN_CLOSED # 执行结束
def simple_coroutine():
    print("-> coroutine start")
    x = yield#yield 默认返回None.如果协程只需要从客户那里接收数据，yield关键字右边不需要加表达式
    print("-> coroutine received:",x)

c1 = simple_coroutine()
c1
print(inspect.getgeneratorstate(c1))#获取携程的状态 ，这里是GEN_CREATED  等待开始执行的状态。
c1.send(None) # 此时协程处于 GEN_SUSPENDED (在yield表达式处暂停) 并且 当协程处于暂停状态才能调用send方法。
# next(c1) #next(c1)可以达到相同的效果。

print(inspect.getgeneratorstate(c1))
try:
    c1.send(666)
except StopIteration:
    pass
print(inspect.getgeneratorstate(c1))

print("|"*66)


def simple_coro2(a):
    print("coroutine start :a=",a)
    b=yield a
    print("recevied b:",a,b)
    c=yield a+b
    print("recevied c:",a,b,c)

c2 = simple_coro2(5)
print(inspect.getgeneratorstate(c2))

next(c2)
print(inspect.getgeneratorstate(c2))

c2.send(6)
print(inspect.getgeneratorstate(c2))
try:
    c2.send(7)
except StopIteration:
    pass

def avg():
    total=0.0
    count=0
    avg=None

    while 1:
        num = yield  avg
        total +=num
        count+=1
        avg=total/count

aa=avg()
print(aa.send(None))
for i in range(0,50,10):
    print(aa.send(i))

print("$"*66)

class testExcept(Exception):
    def handle_exception(self):
        print("start")
        while 1:
            try:
                x=yield
            except testExcept:
                print("run  test Except")
            else:
                print("recived x:",x)
        raise RuntimeError("this line not run.")

