import asyncio

# @asyncio.coroutine
# def wget(host):
#     print("wget (%s)" % host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     header ='''GET /weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=5&isTitle=0&noborder=0&isWeibo=0&isFans=0&uid=1658384301&verifier=078cedea&colors=0593d3,ffffff,666666,0593d3,0477ab&dpc=1 HTTP/1.1
# Host: widget.weibo.com
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
# Cookie: _s_tentry=-; Apache=886212731512.7433.1515382818826; SINAGLOBAL=886212731512.7433.1515382818826; ULV=1515382819686:1:1:1:886212731512.7433.1515382818826:; HAVAR=usrmdinst_4
# If-Modified-Since: Tue, 09 Jan 2018 07:54:57 GMT'''
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print()

def fab3(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b= b,b+a
        n+=1

a= fab3(10)
print(a)
print('-----')
for i in a:
    print(i,end='\n-----\n')

def bbb():
    yield  from (x for x in range(10))

for i in bbb():
    print(i)
import  threading

@asyncio.coroutine
def hello(index):
    print("hello 111 :%s,thread: %s" % ( index,threading.currentThread()))
    yield from asyncio.sleep(2)
    print( "hello 222 :%s,thread: %s" % ( index,threading.currentThread())  )

loop= asyncio.get_event_loop()
tasks = [hello(x) for x in range(10) ]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()


import aiohttp
async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(url,resp.status)
            print(url,await resp.text())

loop = asyncio.new_event_loop()
tasks= [get("http://www.qianfanedu.cn/forum-195-%s.html" % str(x) )   for  x  in range(2,10)  ]
# tasks= [get("http://www.qianfanedu.cn/forum-195-5.html") , get("http://www.qianfanedu.cn/forum-195-6.html") ,get("http://www.qianfanedu.cn/forum-195-7.html")  ]
loop.run_until_complete(asyncio.wait(tasks))
loop   .close()