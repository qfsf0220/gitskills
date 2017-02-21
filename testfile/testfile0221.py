
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
        print("id:{},name:{},age:{}".format(self.n,self.i,self.a))

b=test2("qf",1,29)
b.printino()
