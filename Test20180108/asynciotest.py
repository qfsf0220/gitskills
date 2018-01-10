import asyncio,time

now = lambda :time.time()

@asyncio.coroutine
def a(x):
    print("hello",x)

start = now()

corou = a("qqqq")

loop = asyncio.get_event_loop()

task= loop.create_task(corou)
print(task)
loop.run_until_complete(task)
print(task)
print("used:",now()-start)


import threading
@asyncio.coroutine
def b():
    print("111111(%s)" % threading.currentThread())
    yield from asyncio.sleep(2)
    print("222222(%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [b(),b()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()