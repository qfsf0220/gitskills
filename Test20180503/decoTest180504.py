def dec(func):
    print("11111")
    func()
    print("22222")
    return func

@dec
def a():
    print(123)


# a= dec(a)
# a()
print("-"*20)
def x(a):
    def y(b):
        print("y")
        print(a)
        return(b)
    return y

@x(123)
def z(a):
    print(a)
z(1)




