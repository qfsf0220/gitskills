import  asyncio
import time
now= lambda :time.time()

async def do(x):
    print("waiting:",x)
    await asyncio.sleep(x)
    return "done after {}s".format(x)

start = now()
coroutine1 = do(1)
coroutine2 = do(2)
coroutine3 = do(4)

tasks= [asyncio.ensure_future(coroutine1),asyncio.ensure_future(coroutine2),asyncio.ensure_future(coroutine3)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks)) #这里也可以。loop.run_until_complete(asyncio.gather(*tasks)) 这里是接受一堆task对象

for i in tasks:
    print("task ret:",i.result())
print("time :",now()-start)


print("---"*20)

async def main():
    coroutine1 = do(1)
    coroutine2 = do(2)
    coroutine3 = do(4)
    tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2), asyncio.ensure_future(coroutine3)]
    ''''''
    dones,pendings = await asyncio.wait(tasks)
    for i in dones:
        print("Task ret :",i.result())
    '''
    方法2：上面如果使用的是asyncio.gather创建协程对象，那await的返回值就是协程的运行结果
    results= await asyncio.gather(*tasks)
    for i in results:
        print("Task ret :", i)

    方法3：也可以使用asyncio.as_completed
async def main():
    coroutine1 = do(1)
    coroutine2 = do(2)
    coroutine3 = do(4)
    tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2), asyncio.ensure_future(coroutine3)]

    for i in asyncio.as_completed(taks):
        result = await i
        print("Task ret: {}".format(result))

    loop = asyncio.get_event_loop()
    done = loop.run_until_complete( main())
    print('TIME: ', now() - start)
    '''

start  = now()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('TIME: ', now() - start)
