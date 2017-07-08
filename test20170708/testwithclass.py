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
     def __init__(self,a,b,c):
         self.a=a
         self.b=b
         self.c=20

     def info(self):
         print(self.a,self.c)

if __name__=="__main__":
    a=aaa(1,2,3)
    a.info()

