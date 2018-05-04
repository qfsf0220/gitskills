def a(num):

    def b():
        return (num)
    return  b

def c(num):
    print("%x" % id(num)) # %x 通过16进制打印 num的ID值
    flag = 5
    if num > flag:
        print("ok")
    else:
        print("failed")
    def d():
        print("num:",num,"\n---------")
    d()
    return d

x= c(222)
print(x.__closure__) #  这里int对象 值等于 numID值  指向了num的内存地址
x() #--> return 的 d

print("++"*10)

f= a(5)
print(f())
print("-{-{-{"*10)


def ff(aa):
    def  gg(bb):
        if bb >aa:
            print("ok")
        else:
            print("failed")
    return gg

getff = ff(5)   #这里形参是aa getff
print(type(getff))
print(getff.__closure__)

getff(2)


print("*******************"*3)

def my_sum(*aaa):
    if len(aaa) ==0:
        return "can not sum"
    for i in aaa:
        if not isinstance(i,int):
            return "can not sum"
    return sum(aaa)

def my_average(*aaa):
    if len(aaa) ==0:
        return "can not average"
    for i in aaa:
        if not isinstance(i,int):
            return "can not average"
    return sum(aaa)/len(aaa)

print(my_sum(1, 2, 3, 4, '5'))
print(my_average(1, 2, 3, 4, '5'))

def mysum(*a):
    return sum(a)
def myavg(*a):
    return sum(a)/len(a)


def bibaofunc(func):
    def inthefunc(*aa):
        print("func:",func)
        print("aa:",aa)
        return func(*aa)
    return inthefunc

mysum  = bibaofunc(mysum)
print("mysum:",mysum)
print(mysum(1,2,3))


@bibaofunc
def mysum2(*a):
    print(sum(a))

mysum2(1,2,3,4)


