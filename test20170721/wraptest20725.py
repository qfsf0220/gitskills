class c1:
    def __init__(self):
        pass
    @staticmethod
    def c1func1():
        print('c1f1---'*20)
    @staticmethod
    def c1func2():
        print('c1f2---'*20)

class  c2:
    def __init__(self):
        pass
    @staticmethod
    def c1func1():
        print('c2f1---'*20)
    @staticmethod
    def c1func2():
        print('c2f2---'*20)

def abc(arg):
    def _a(func):
        def __a(*a,**aa):
            arg.c1func1()
            func(*a,**aa)
            arg.c1func2()
        return __a
    return _a
