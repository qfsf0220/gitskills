#-*- coding:utf-8 -*-
# import datetime
#
# a = 0
# for i in range(1, 11):
#     a += i
#
# print a
#
# print datetime.datetime.now()
#
#
# class Student(object):
#     a = 'qq'
#     pass
#
# s = Student()
# print(s.a)
#
#
# def set_age(self, age):
#     self.age = age
#
#
# from types import MethodType
# s.set_age=MethodType(set_age, s)
# s.set_age(28)
# print(s.age)
#
# s2=Student()
# s2.set_age=MethodType(set_age, s2)
# s2.set_age(27)
# print(s2.age)
#
#
# def set_score(self,score):
#     self.score=score
#
# Student.set_score=set_score
#
# s.set_score(100)
# s2.set_score(99)
# print (s.score,s2.score)
#
# class Student2(object):
#     __slots__ = ('name', 'age', 'address')
# s3=Student2()
#
# s3.name='qf'
# s3.age=29
# s3.address='shanghai xuhui'
# # s3.score='it is disapprove'
# print(s3.name,s3.age,s3.address,)
#
# class Student3(object):
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score is an integer!!')
#         if value<0 or value>100:
#             raise ValueError('range is 0-100!!')
#         self.score=value
#
# s=Student3()
# # s.set_score(999)
# s.set_score(95)
#
# print(s.get_score())
#
# # class Student4(object):
# #     @property
# #     def score(self):
# #         return self.score
# #
# #     @score.setter
# #     def score(self,value):
# #         if not isinstance(value, int):
# #             raise ValueError('score is an integer!!')
# #         if value < 0 or value > 100:
# #             raise ValueError('range is 0-100!!')
# #         self.score = value
# #
# # s=Student4()
# # s.score=60
# # print(s.score)
#
# class Animal(object):
#     pass
# class Mammal(Animal):
#     pass
# class Bird(Animal):
#     pass
#
# class runnable(object):
#     def run(self):
#         print ('i can run')
# class flyable(object):
#     def fly(self):
#         print ('i can fly')
# class CarnivorousMixIn(object):
#     def eatmeat(self):
#         print('i like meat')
# class HerbivoresMixIn(object):
#     def eatplant(self):
#         print ('i like plant')
#
#
# class dog(Mammal,runnable,CarnivorousMixIn):
#     pass
# class bat(Mammal,flyable):
#     pass
# class parrot(Bird,flyable):
#     pass
# class Ostrich(Bird,runnable):
#     pass
#
#
#
#
# class qf(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'qf object(name:%s)' %self.name
#
# print(qf('qianfeng'))
#
# q=qf('woshiqianfeng')




# class test(object):
#     def __init__(self,age,name,score):
#         self.name=name
#         self.age=age
#         self.score=score
#
#     def print_info(self):
#         print ('old guy(%s)！弄叫%s啊--yous core:%s'%(self.age,self.name,self.score))
#
#     def get_grade(self):
#         if self.score>=90:
#             return 'A'
#         elif self.score>=60:
#             return 'B'
#         else:
#             return 'C'
#
#     def set_score(self,score):
#         if 0<=score<=100:
#             self.__score=score
#         else:
#             raise IndexError('温馨提示：this is a bad score(1-100)')
#
#
# test=test(29,'qf',88)
#
# test.set_score(98)
# test.print_info()
#
# print(test.get_grade())

class Animal(object):
    def run(self):
        print(" runnnning ...")

class Dog(Animal):
    print("i am dog")
    pass

class Cat(Animal):
    def run(self):
        print ('i am cat ,i am running.')

print '*'*20
def runx2(a):
    a.run()
    a.run()

runx2(Cat())

# a=list()
# b=Animal()
# c=Dog()
#
#
# def run2(a):
#     a.run()
#     a.run()
#
#
# run2(Dog())