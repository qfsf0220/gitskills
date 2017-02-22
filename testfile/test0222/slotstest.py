class a:
    pass

s=a()
s.name = "qf0222"
print(s.name)

#给实例绑定一个方法
def set_age(self,age):
    self.age=age

from types import MethodType

s.set_age = MethodType(set_age,s)#给实例绑定一个方法

s.set_age(25)
print(s.age)
#给一个实例绑定的方法，对另一个实例是不起作用的
s2= a()
#s2.setage(25)#这里报 AttributeError 错误

#为了给所有实例绑定方法 可以给class绑定方法
def set_score(self,score):
    self.score = score

a.set_score=set_score

s.set_score(88)
print(s.score)
s2.set_score(99)
print(s2.score)

#如果我们想要限制实例的属性
#在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性
class b:
    __slots__ =('name','age')

bb=b()
bb.name="qf"
bb.age=25
# bb.score=88 //slots 允许name age  但是没有score 所以 实例添加score 报错
#slots 对继承子类无效。