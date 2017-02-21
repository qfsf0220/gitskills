class a:
    def __init__(self,name,score,id):
        self.__n = name
        self.__s = score
        self.i = id =1

    def printscore(self):
        print("%s -- %s"%(self.__n , self.__s))

a=a("qf",99,1)
#print   (a.__s) #这里_-- 表示为 私有属性  无法直接使用了。
print(a.i)  #i 可以正常使用。

a.printscore()
