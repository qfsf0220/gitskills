import asyncio

@asyncio.coroutine
def a():
    print(1)
    r= yield  from asyncio.sleep(1)
    print(2)

a()

async def b():
    print(1)
    r=await asyncio.sleep(1)
    print(2)


print(b())
print("---")
b().send(None)

import select
import socket

def coroutine():
    sock = socket.socket()
    sock.setblocking(0)
    address = yield sock
    try:
        sock.connect(address)
    except BlockingIOError:
        pass
    data = yield
    size = yield sock.send(data)
    yield sock.recv(size)


def main():
    coro = coroutine()
    sock = coro.send(None)
    wait_list = (sock.fileno(),)
    coro.send(('www.baidu.com', 80))
    select.select((), wait_list, ())
    coro.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: Close\r\n\r\n')
    select.select(wait_list, (), ())
    print(coro.send(1024))
import select
import socket


def coroutine():
    sock = socket.socket()
    sock.setblocking(0)
    address = yield sock
    try:
        sock.connect(address)
    except BlockingIOError:
        pass
    data = yield
    size = yield sock.send(data)
    yield sock.recv(size)


def main():
    coro = coroutine()
    sock = coro.send(None)
    wait_list = (sock.fileno(),)
    coro.send(('www.baidu.com', 80))
    select.select((), wait_list, ())
    coro.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: Close\r\n\r\n')
    select.select(wait_list, (), ())
    print(coro.send(1024))


if __name__ == '__main__':
    main()