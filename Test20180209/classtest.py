class Test:
    def abc(self,x,y):
        self.x=x
        self.y=y
    def set(self):
        self.abc(1,2)
        print("set ok")

    def resultnum(self,othernum):
        return (self.x+othernum)**2 +(self.y+othernum)**2


t1 = Test()
t1.set()
print(t1.resultnum(100))

t2=Test()
t2.abc(5,6)
print(t2.resultnum(100))
