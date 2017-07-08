from test20170708.testwithclass import  aaa

a=aaa(1,2)
a.info2()
a.info()

class  ttt:
    def __init__(self):
        self.x=10;
        self.y=20;

    def outxy(self):
        return (self.x,self.y)

    def printinfo(self):
        print(self.outxy()[0],'---',self.outxy()[1])
# ttt=ttt()
#
# ttt.printinfo()

class rrr(ttt):
    def echo1(self):
        print(1111)
    def printinfo(self):
        print(self.x,'@@@',self.y)


rr=rrr()
rr.printinfo()
rr.echo1()

print(isinstance(rr,ttt)) #参数1 实例 参数2 类名
print(isinstance(rr,rrr))

def threetime(x):
    x.printinfo()
    x.printinfo()
    x.printinfo()

threetime(rrr())
