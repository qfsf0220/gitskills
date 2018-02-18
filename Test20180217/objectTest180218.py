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