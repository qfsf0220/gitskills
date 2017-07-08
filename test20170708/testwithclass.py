# class testclass:
#     def sss(self):
#         self.a=20
#         print(self.a)
#     b = 30
#
# a = testclass()
#
# print(a.sss())
class aaa:
    thisisaclassattribute='iamaclassattr.'
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=20
        self.__a=5678

    def info(self):
        print(self.a,self.c)
    def info2(self):
        print(self.__a)

    def define_d(self,d):
        self.d=d;

if __name__=="__main__":
    a=aaa(1,2)
    a.info()
    a.define_d(78910)
    print(a.d)
    a.__a=1234
    a.info2()#这里是内部访问无法改变__a值
    print(a.__a) #这里是外部访问  a.__a 所以是1234
    #另外一种是_a 这个是标志性私有变量 外部也是可以改变_a的值得，非强制性。

