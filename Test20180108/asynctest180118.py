import asyncio

def coro1():
    print("c1:start")
    print("c1:end")

def coro2():
    print("c2:start")
    print("c2:a")
    print("c2:b")
    print("c2:c")
    print("c2:end")

# async def coro1():
#     print("c1:start")
#     print("c1:end")
#
# async def coro2():
#     print("c2:start")
#     print("c2:a")
#     print("c2:b")
#     print("c2:c")
#     print("c2:end")

#
# print(c1)

# try:
#     c2.send(None)
# except:
#     pass


print("|"*50)
@asyncio.coroutine
def switch():
    yield

async def coro1():
    print("c1 :start")
    await switch()
    print("c1:end")

async def coro2():
    print("c2:start")
    print("c2:a")
    print("c2:b")
    print("c2:c")
    print("c2:end")

c1 =coro1()
c2 = coro2()
#
# try:
#     c1.send(None)
# except StopIteration:
#     pass
# try:
#     c2.send(None)
# except StopIteration:
#     pass
# try:
#     c1.send(None)
# except StopIteration:
#     pass

def run(coros):
    coros = list(coros)

    while coros:
        for i in coros:
            try:
                i.send(None)
            except StopIteration:
                coros.remove(i)

run([c1,c2])