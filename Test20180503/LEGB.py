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
