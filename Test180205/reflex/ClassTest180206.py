class shiquren:
    name = ""

class bendiren:
    bname = "awuluan"#静态字段 （类变量）

    def __init__(self,isshiqu,siyouziduan):
        self.iname= "qf"#动态字段 局部变量
        self.youareshiquman=isshiqu #同上 但是需要实例化时 传入形参
        self.__qiong =siyouziduan #这里设置了私有字段  __qiong

    def getsiyouziduan(self): #定义一个公有方法，类内部可以访问私有字段
        return("私有字段: 穷不穷？"+str(self.__qiong))

    def shumucunguang(self): #动态方法 鼠目寸光
        print(self.iname+"鼠目寸光")

    def __siyoufangfa(self):#私有方法
        print("siyou class")
    def getsiyoufangfa(self):#定义一个公有方法
        self.__siyoufangfa() # 内部可以访问私有方法
    #获取私有字段的第二种方法 通过property
    @property#只读
    def getqiongbuqiong(self): #通过特性直接访问__qiong这个私有字段，这里是 只读这个私有字段的
        return (self.__qiong)
    #如果需要修改这个私有字段，需要这样绕圈子
    @getqiongbuqiong.setter #设置为可写 但是本类需要继承object类 即：bendiren(object)
    def setsiyouziduan(self,abc): #通过abc这个形参 来给私有字段__qiong赋值
        self.__qiong=abc

    @staticmethod  #内置方法staticmethod 把方法定义为静态方法
    def xiangbuchuan():#静态方法 想不穿 静态方法属于类 所以不需要实例化为对象，所以不需要self
        print(bendiren.bname+"想不穿") #创建静态方法，往往可以减少实例化时所占用的内存资源

    @property #通过property方法 可以把方法 变成为属性(一般称为：特性)
    def chun(self):
        print(self.bname+" fatuous.")
        return(self.bname+" fatuous.") #这里返回值 等于chun这个特性现在是xxxfatuous 这个string


    def __del__(self):#析构函数 对象没人用了就销毁，这个方法在销毁的时候运行。
        print("Done.")
    def __call__(self, *args, **kwargs):
        print("this is call")

b3 =bendiren(1,2)  #bendiren这个类后面带一个括号 就是等于执行了类的构造函数（即实例化的时候需要调用）
b3() #对象+括号直接 等于直接运行 类里面的__call__方法  ，__call__方法 是一个特殊方法
bendiren('a',5)() #这里 bendiren(x,x) 就是一个对象  对象+()  就是执行__call__方法

s1 = shiquren()
s1.name="boss zhang"
print(s1.name)

print(bendiren.bname)#直接调用类变量 name
b1 = bendiren(False,True) #实例化 本地人类 为 b1
print(b1.iname)  #获取 class构造函数初始化以后的name
print(b1.bname)#方法可以访问类变量 类不能访问局部变量（只能从内到外,一般不直接访问）
b1.shumucunguang() #b1 执行shumucunguang 方法 （类不能直接执行动态方法（局部方法））
b2=bendiren(False,True) #实例化b2 传入 你是市区人 的形参 false
b2.iname="JY"  #直接设置b2的 iname
b2.shumucunguang() # 同b1
bendiren.xiangbuchuan() #类直接调用静态方法（类不能调用鼠目寸光这个动态方法）
b2.xiangbuchuan()#对象调用 静态方法
b1.chun #直接调用property 修饰的动态方法 ，不用加 小括号,看上去直接访问了属性（特性）。
# print(b2.__qiong) #双下划线 私有字段无法直接访问 可以通过添加一个getxx来访问（这里体现了封装性）
print(b1.getsiyouziduan()) #这里用getxx方法 间接获取私有字段。
b1.getsiyoufangfa() #间接访问 私有方法
print(b1.getqiongbuqiong) #通过property获取私有字段，封装性的体现，常用于无法更改的字段
b1._bendiren__siyoufangfa()###强行 调用私有方法（一般不用 需要绕圈子）
#这里绕圈子
b1.setsiyouziduan = "raoraorao"#对实例
print(b1.getqiongbuqiong)

#这里创建class father 不用加(object) py2需要继承自object类才是新式类，不加的都是经典类
#py3开始默认都是新式类，相对方法多一些， 继承搜索顺序不同。
class Father:
    def __init__(self):
        self.name="ff"
        print("__init__调用测试")

    def funcfa(self):
        print("farther func")
    def funcfa2(self):
        print("fa func2")

#
class Son(Father): #这里继承 father类
# class Son(Father,bendiren,shiquren): #多重继承 father bendiren shiquren
#多继承 中 所继承的父类 是有优先级的 是 从左往右 找 如果有同样方法 先继承左面的父类
    def __init__(self):
        self.name="ss"
        Father.__init__(self) #显式调用父类的构造方法 （1）
        # super(Son,self).__init__() # 调用父类的构造方法 （2）
    def funcso(self):
        print("son func")
    def funcfa2(self): #重写 父类的 funcfa2 方法
        print("change to son func2")
    def funcfa(self):
        Father.funcfa(self)
        print("addtion son func")

print("++"*10)
s1 = Son()
s1.funcfa() #通过子类对象 调用父类方法








