import aiohttp
import asyncio
import random,time
from pyquery import PyQuery as pq
async def tttt(session,url):
    with aiohttp.Timeout(10):
        async with session.get(url) as r:
            print(url)
            doc = pq(await r.text())
            print(doc("body > div.content > div.subnav > div.subnav-title > div.subnav-title-name > a").text())
now = lambda :time.time()
a= now()
loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
session = aiohttp.ClientSession(loop=loop)
tasks=[]
for url in ['https://www.autohome.com.cn/{}/price.html'.format(random.randint(10,1000)) for i in range(50)]:
    tasks.append(tttt(session,url))
loop.run_until_complete(asyncio.gather(*tasks))
session.close()
b=now()
print("用时:"+ str(b-a))
