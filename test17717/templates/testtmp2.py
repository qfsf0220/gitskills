from testtmp import *

class example:
    @a(aaa)
    def t2func(self):
        print('t2func')

    @a(aaa)
    @a(bbb)
    def t2func2(self,a,b):
        print('t2func2'+str(a)+str(b))



if __name__ =='__main__':
    ex=example()
    ex.t2func()
    ex.t2func2(5,80)