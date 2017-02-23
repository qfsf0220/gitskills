#多重继承只限于python 入java只允许单一继承 不能使用mixin设计
class human:
    pass

class woman(human):
    pass

class man(human):
    pass

class girl(woman):
    def sayhi(self):
        print("hello i am girl")

class boy(man):
    def sayhi(self):
        print("hi  i am a boy")


class mary(girl):
    pass

class tom(boy):
    def sayhi(self):
        print("hi i am Tom")

class singable(human):
    def sing(self):
        print("singing")

class danceable(human):
    def dance(self):
        print("danceing")

class tom(human,boy,singable):
    pass

tom = tom()
tom.sing()
tom.sayhi()