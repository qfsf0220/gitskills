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

s=Student2()
print(s.name)
print(Student2.name)
s.name = "new name"
print(s.name)
print(Student2.name)
del s.name

print(s.name)
#这里看到 相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。