class Student:
    def __init__(self,name):
        self.name = name

#由于Python是动态语言，根据类创建的实例可以任意绑定属性。
s=Student("qf") #s为实例
s.score = 90   #直接绑定属性

print(s.name)
print(s.score)


class Student2:
    name = "Student2"

s=Student2() # 创建实例s
print(s.name)# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student2.name)# 打印类的name属性
s.name = "new name"# 给实例绑定name属性
print(s.name)# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student2.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性

print(s.name)# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#这里看到 相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。