class ccc:
    def __init__(self):
        print('__init__ will not run')
    @staticmethod
    def func1():
        print('1'*20)
    @staticmethod
    def func2():
        print('2'*20)

def abc(arg):
    def _a(func):
        def __a(*a,**aa):
            arg.func1()
            func(*a,**aa)
            arg.func2()
        return __a
    return _a

@abc(ccc)
def myfunc():
    print('this is myfunction.')

myfunc()

