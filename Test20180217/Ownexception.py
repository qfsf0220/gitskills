class  buduile(Exception):
    pass

# raise buduile("this is a own exception test")
class budui2(Exception):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        if self.a>self.b:#there will not be run
            return ( "error (a>b) ..") #zheli buhui zhixing



class buduio(Exception): #full version
    def __init__(self,a,b):
        super().__init__(" {} is  not ok".format(b) )
        self.a=a
        self.b=b
    def xx(self):
        return self.b-self.a
try:
    raise buduio(5,66)
except buduio as e:
    print(e)
    print("more than <"+str(  e.xx()  )+"> is ok")

try:
    raise budui2("exception message is this as a ","messge2 as b")
except budui2 as e:
    print(e)


