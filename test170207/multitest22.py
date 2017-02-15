import multiprocessing
import  random
import  time

def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % (
        multiprocessing.current_process().name,
        func.__name__, args, result
        )
def calculatestar(args):
    return calculate(*args)

def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b


def test():
    print(multiprocessing.cpu_count())#4

    pool = multiprocessing.Pool(4)
    print()

    TASK = [a for a in range(10)]+[b for b  in range(20,30)]

    resault = [pool.apply_async(calculate,t) for t in TASK]
    imap_it = pool.imap(calculatestar,TASK)
