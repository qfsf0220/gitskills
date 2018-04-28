import asyncio
import time
time1 = time.time()
async def aaa(x):
    print("Wait...:",x)
time2= time.time()
coroutine = aaa(2)
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print("Time :", time.time()-time2)

print("---"*20)

async def  bbb(x):
    print("2222Wait:",x)
coroutine2 = bbb(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine2)
print(task)
loop.run_until_complete(task)

print("---"*20)

async def ccc(x):
    print(x*11)

def callback(future):
    print("Callback: " , future.result())

coroutine3 = ccc(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine3)
task.add_done_callback(callback)
loop.run_until_complete(task)

print("---"*20)
async def ddd(x):
    print("Wait:",x)
    return "Done after {}s".format(x)
start = time.time()
coroutine4 = ddd(2)
loop = asyncio.get_event_loop()
task = asyncio  .ensure_future(coroutine4)
loop.run_until_complete(task)
print('Task ret: {}'.format(task.result()))
print('TIME: {}'.format(time.time() - start))

print("---"*20)
async def eee(x):
    print("wait",x)
    await asyncio.sleep(x)
    return "done after {}s".format(x)
start = time.time()
coroutine5 =eee(2)
loop=asyncio.get_event_loop()
task =asyncio.ensure_future(coroutine5)
loop.run_until_complete(task)

print('Task ret: ', task.result())
print('TIME: ', time.time() - start)





