import asyncio
import time
"""使用async可以定义协程，协程用于耗时的io操作，我们也可以封装更多的io操作过程，这样就实现了嵌套的协程，即一个协程中await了另外一个协程，如此连接起来。"""

now = lambda :time.time()
async def do_sth(x):
    print("waiting:",x)
    await asyncio.sleep(x)
    return "done after {}s".format(x)

async def main():
    coroutine1=do_sth(2)
    coroutine2=do_sth(4)
    coroutine3 =do_sth(6)
    tasks=[
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    # dones, pending = await asyncio.wait(tasks)
    # for task in dones:
    #     print("Task ret:",task.result())
    results= await asyncio.gather(*tasks)
    for i in results:
        print("task ret :",i)

start=now()

loop   =asyncio.get_event_loop()
loop.run_until_complete(main())
print("cost:",now()-start ,"秒")