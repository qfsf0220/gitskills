import asyncio
import time
def myfun(i):  #这里使用普通的time.sleep()作为等待。则需要通过添加线程的方式实异步。
    print('start {}th'.format(i))
    time.sleep(1)
    print('finish {}th'.format(i))

async def main():
    loop = asyncio.get_event_loop()
    futures = (loop.run_in_executor(None, myfun,i)  #这里  run_in_executor其实是开启了一个新的线程，再协调各个线程。
               for i in range(10) )
    for result in await asyncio.gather(*futures):
        pass
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("++" * 30)
#上面10次循环仍然不是一次性打印出来的，而是像分批次一样打印出来的。这是因为开启的线程不够多，如果想要实现一次打印，可以开启10个线程
import concurrent.futures as  cf
import  asyncio ,time
def myfunc2(i):
    print("start {}th" .format(i))
    time.sleep(1)
    print("end {}th".format(i))

async def main():
    with cf.ThreadPoolExecutor(max_workers=10) as executor:#这里设置了10个线程
        loop=asyncio.get_event_loop()
        futures = (
            loop.run_in_executor(executor,   #按照10个线程来执行
                                 myfunc2,i)  for i in range(10) )
        for  result in await asyncio.gather(*futures):
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())