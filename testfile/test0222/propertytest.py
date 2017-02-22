#Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('not a integer')
        if value<0 or value>100:
            raise ValueError('out of 0~100')
        self._score = value


s=Student()

s.score=60
print(s.score)

#s.score = 101#print(s.score) #这里会raise value错误

class body:
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id = value

    @property
    def age(self):
        return 123+self._id

body = body()
body._id = 10;
print(body.age)