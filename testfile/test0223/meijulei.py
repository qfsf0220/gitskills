from enum import Enum


Month = Enum("Month",('jan','feb','mar','apr','may','jun','jul',
                      'aug','sep','oct','nov','dec'))

for name,member in Month.__members__.items():
    print(name,"=>",member,',',member.value)


from enum import unique

@unique  #@unique装饰器可以帮助我们检查保证没有重复值。
class aa(Enum):
    sun=0
    mon =1
    tue = 2
    wed =3
    thu = 4
    fri = 5
    sat = 6

#访问枚举类型值
day1 = aa.mon
print(day1)
print(aa['sat'])
print(aa.sun.value)
print(day1 == aa.thu)
print(aa(2))

for a,b in aa.__members__.items():
    print(a,b)
