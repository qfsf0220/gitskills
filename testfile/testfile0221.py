
class testtest:
    def __init__(self,name='qqqq'):
        self.name= name
        print("initializes the  %s" % self.name)



a=testtest('nonghao')


class test2(object):
    def __init__(self,name,id,age):
        self.n =name
        self.i = id
        self.a = age

    def printino(self):
        print("id:{},name:{},age:{}".format(self.n, self.i, self.a))

b = test2("qf", 1, 29)
b.printino()

#重写
class A:
    def hello(self):
        print("AAAAA")

class B(A):
    pass

class C(A):
    def hello2(self):
        print("ccccc")
b=C()
b.hello()
b.hello2()

#属性
class area:
    def __init__(self):
        self.width = 0
        self.height = 0
    #
    # def setsize(self,size):
    #     self.height,self.width=size

    def getsize(self):
        return self.height*self.width

area = area()
area.width=10
area.height=20
print(area.getsize())