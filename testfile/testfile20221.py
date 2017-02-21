class a:
    def __init__(self,a,b):
        self.b=b
        self.a =a

    def printab(self):
        print("-----%s      %s-----"%(self.a,self.b))

a=a('z','c')
a.printab()


class a2:
    def __init__(self,score,name):
        self.score = score
        self.name = name

    def get_grade(self):
        if self.score >90:
            print("A")
        elif self.score >60:
            print("B"+self.name)
        else:
            print("C")

a2=a2(88,'八十八分')
a2.get_grade()