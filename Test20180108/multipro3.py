from multiprocessing import Pool
import random
from functools import reduce

# def f(g):
#     return  reduce(lambda x,y:str(x)+str(y) ,[random.randint(1,10) for x in range(20)])
#
#
#
# if __name__=="__main__":
#     p=Pool(4)
#     print(p.map(f,[1,2,3]))
def odd():
    n=1
    while True:
        yield n
        n+=2

a= odd()
b=6
while b>0:
    print(next(a))
    b-=1
