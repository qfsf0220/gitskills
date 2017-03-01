import time
import threading


class Test(threading.Thread):
    def __init__(self, name, delay):
        super(Test, self).__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print "%s delay for %s seconds" % (self.name, self.delay)
        time.sleep(self.delay)
        c = 0
        while True:
            print "This is thread %s on line %s" % (self.name, c)
            c += 1
            if c == 3:
                print "End of thread %s" % self.name
                break


t1 = Test('Thread1', 10)
t2 = Test('Thread2', 10)

t1.start()
print 'Wait t1 to end'
t1.join()
t2.start()
t2.join()
print 'done==========='