import multiprocessing
import  time
import random,os
from functools import reduce

#
# # def worker(aaa):
# #     n = 5;
# #     while n>0:
# #         print("%s start: %s" % (os.getpid(),time.ctime()))
# #         print (reduce(lambda x,y:str(x)+str(y),[random.randint(0,10) for x in range(20)]) )
# #         time.sleep(1)
# #         print("%s end: %s" % (os.getpid(), time.ctime()))
# #         n-=1
# #
# # if __name__=='__main__':
# #     p=multiprocessing.Process(target=worker,args=(2,),name="test1")
# #     p.daemon =True
# #     p.start()
# #     p.join()
# #     print("t1 sub pid:"+str(p.pid))
# #     print("t1 name:"+str(p.name))
# #     print("t1 alive:"+str(p.is_alive()))
# #
# #     p2=multiprocessing.Process(target=worker,args=(3,),name="test2 ")
# #     p2.daemon = True
# #     p2.start()
# #     print("t2 sub pid:" + str(p.pid))
# #     print("t2 name:" + str(p.name))
# #     print("t2 alive:" + str(p.is_alive()))
# a = []
# b=[]
# def  runproc():
#     print("msg:",os.getpid(),"~~~",os.getppid())
#     time.sleep(1)
#     return("msg:",os.getpid(),"~~~",os.getppid())
#
#     # a.append(reduce(lambda x,y:str(x)+str(y) ,[random.randint(1,10) for x in range(20)])
#
#
# class tspro(multiprocessing.Process):
#     def __init__(self):
#         multiprocessing.Process.__init__(self)
#
#     def run2(self):
#         for i in range(5):
#             print("now %s" % time.ctime())
#
#
#
# if __name__=="__main__":
#     # p=multiprocessing.Pool(6)
#     #
#     # for i in range(10):
#     #     a.append(p.apply_async(runproc) )
#     #
#     # print("start")
#     # p.close()
#     # p.join()
#     #
#     #
#     # print("All Done ")
#     # print(2)
#     p2 = tspro()
#     p2.start()
#
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()