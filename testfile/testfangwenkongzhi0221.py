class a:
    def __init__(self,name,score,id):
        self.__n = name
        self.__s = score
        self.i = id =1

    def printscore(self):
        print("%s -- %s"%(self.__n , self.__s))

    # 如果为了外部代码访问 属性 需要添加get的方法获取
    def get_name(self):
        return self.__n
    def get_score(self):
        return self.__s
    #如果 为了外部修改 属性  添加 set方法
    #原先那种直接通过bart.score = 59也可以修改啊，\
    # 为什么要定义一个方法大费周折？因为在方法中，
    # 可以对参数做检查，避免传入无效的参数：
    def set_score(self,score):
        if 0<=score <=100:
            self.__s =score
        else:
            raise ValueError("out of 0~100")


a=a("qf",88,1)
# #print   (a.__s) #这里_-- 表示为 私有属性  无法直接使用了。
# print(a.i)  #i 可以正常使用。
# a.set_score(100) #这里如果不是0到100 会报错。
# a.printscore()
print(a.get_name())
#错误写法
#表面上看，外部代码“成功”地设置了__
# name变量，但实际上这个__name变量和class内部的__name变量
# 不是一个变量！内部的__name变量已经被Python解释器
# 自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
a.__name = 'new name'
print(a.__name)
print(a.get_name())