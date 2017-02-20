from gevent import monkey;
monkey.patch_socket();
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0) #实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换，

g1 = gevent.spawn(f,50000)
g2 = gevent.spawn(f,50000)
g3 = gevent.spawn(f,50000)
g1.join()
# g2.join()


