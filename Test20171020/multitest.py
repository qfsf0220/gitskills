import multiprocessing
import  time


def process(num):
    print("process:",num)

if __name__ == '__main__':
    for i in range(5):
        p=multiprocessing.Process(target=process,args=(i,))
        p.start()