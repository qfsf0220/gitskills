class InitTest(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.abc ="abc"

    def echoname(self,name):
        print("my name :"+self.name)
        return (name)

class InitTest22():
    abc="abc2"


it = InitTest("qf",123)
print(it.name)
print("your name:" , it.echoname("qfsf"))
it2 = InitTest22
print("-"*20)
print(it.abc)
print(it2.abc)
print("--"*10)
print(it.__dict__)
print(it2.__dict__)
