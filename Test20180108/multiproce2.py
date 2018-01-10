from  multiprocessing import Lock,Process
import time

def locktest():
    with Lock():
        fs= open("E:\\gitskills\\Test20180108\\123.txt","a+")
        n=10
        while n>1:
            fs.write("lockd\n")
            n-=1
        fs.close()

def locknotest():
    Lock().acquire()
    try:
        fs=open("E:\\gitskills\\Test20180108\\123.txt","a+")
        n=10
        while n>1:
            fs.write("Lock acquired\n")
            n-=1
        fs.close()
    finally:
        pass

if __name__ == "__main__":
    fs = open("E:\\gitskills\\Test20180108\\123.txt", "a+")
    time.sleep(1)
    fs.write("%s" % time.asctime(time.localtime(time.time())))
    w=Process(target=locktest())
    w2=Process(target=locknotest())
    w.start()
    w2.start()

    print("Done")
