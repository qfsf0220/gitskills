class Test:
    def abc(self,x,y):
        self.x=x
        self.y=y
    def set(self):
        self.abc(1,2)
        print("set ok")

    def resultnum(self,othernum):
        return (self.x+othernum)**2 +(self.y+othernum)**2


# t1 = Test()
# t1.set()
# print(t1.resultnum(100))
#
# t2=Test()
# t2.abc(5,6)
# print(t2.resultnum(100))

class passget:
    def __init__(self,username,password):
        self.__user = username
        self.__pass = password

    def decrypt(self,yourpass):
        if yourpass==self.__user:
            print ( self.__pass)

        else:
            print("please retry..")

p1 = passget("asd","this is my pass")
p1.decrypt("asdd")
print(p1._passget__pass)
print("("*22)

class c1:

    wodelist=[]

    def __init__(self,name,age):
        self.name=name
        self.age  =age
        c1.wodelist.append(self)

c1dx=c1('qq',22)
print(type(c1dx))
print(type(c1dx.wodelist[0]))

class c2(c1):
    def addinfo(self,address):
        print(self.name,self.age,address)
c2dx =c2("q",2)
c2dx.addinfo("xh")
print(c1dx.name,c2dx.name,c1dx.age,c2dx.age)



