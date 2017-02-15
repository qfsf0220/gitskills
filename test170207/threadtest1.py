import sys
import threading
import queue

q=queue.Queue()

def w1(x,y):
    fcname= sys._getframe().f_code.co_name
    print("%s"% fcname)
    q.put((x+y,fcname))
def w2(x,y):
    fcname = sys._getframe().f_code.co_name
    print("%s" % fcname)
    q.put((x-y,fcname))
if __name__ == '__main__':
    result = list()
    t1=threading.Thread(target=w1,name='thread1',args=(10,5,))
    t2=threading.Thread(target=w2,name='thread2',args=(20,1,))
    print('-'*22)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    while not q.empty():
        result.append(q.get())
    for item in result:
        if item[1] == w1.__name__:
            print( "%s 's return value is : %s" % (item[1], item[0]) )
        elif item[1] == w2.__name__:
            print( "%s 's return value is : %s" % (item[1], item[0]) )
