from multiprocessing import Process
from multiprocessing.pool import ThreadPool
# a=[]
# def hihi(j):
#     a.append (("hi"+j))
#     print(a)
# #
# # print((hihi("aa")))
# # print(a)
#
# if __name__ == '__main__':
#     for i in str(range(10)):
#         p=Process(target=hihi,args=(i,))
#         p.start()
from  threading import Thread
import time

def fooo(aa):
    time.sleep(10)
    return aa

class Mythread(Thread):
    def __init__(self,number):
        Thread.__init__(self)
        self.number = number

    def run(self):
        self.result = fooo(self.number)

    def get_result(self):
        return self.result

t1=Mythread(3)
t2=Mythread(5)
t1.start()
t2.start()
t1.join()
t2.join()

print(t1.get_result())
print(t2.get_result())