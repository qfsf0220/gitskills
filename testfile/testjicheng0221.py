class Animal(object):
    def run(self):
        print("run")
    def run_twice(animal):
        animal.run()
        animal.run()


class Dog(Animal):
    pass
    def xiao(self):
        print("hoho")

class Cat(Animal):
    def run(self):  #这里是重写animal的函数
        print("cat is run")




d=Dog()
d.run()
d.xiao()
print("cat↓"+"-"*20)
c = Cat()
c.run()

#当子类和父类都存在相同的run()方法时，
# 我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。
m=list()
n=Animal()
o=Dog()
print(
isinstance(m,list),
isinstance(n,Animal),
isinstance(o,Dog),
isinstance(o,Animal),
)


class Tortoise(Animal):
    def run(self):
        print("tortoise is running slowly.")
t=Tortoise()
t.run()
print()
t.run_twice()