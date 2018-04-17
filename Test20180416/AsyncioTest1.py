import asyncio
async def myfun(i):
    print('start {}th'.format(i))
    await asyncio.sleep(2)
    print("finish {}th".format(i))

loop = asyncio.get_event_loop()
myfun_list = (myfun(i) for i in range(10))
loop.run_until_complete(asyncio.gather(*myfun_list))
print("--"*30)
loop2 = asyncio.get_event_loop()
myfun_list2 = [asyncio.ensure_future(myfun(i))  for i in range(10)]
loop2.run_until_complete(asyncio.wait(myfun_list2))