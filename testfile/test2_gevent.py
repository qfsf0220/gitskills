from   gevent import monkey;
monkey.patch_all();
import  gevent
import requests

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/47.0.2526.80 Safari/537.36"}
def f(url):
    print("GET -> %s" % url)
    resp = requests.get(url,verify=True,headers=headers)
    data = resp.text
    print("%d bytes recived from %s" %(len(data),url))

def f2(url):
    print("GET -> %s" % url)
    resp = requests.get(url,verify=True)
    data = resp.text
    print("%s bytes recived from %s" %(data,url))

# gevent.joinall(
#     [
#     gevent.spawn(f,"https://www.python.org/"),
#     gevent.spawn(f,"https://www.yahoo.com/"),
#     gevent.spawn(f,"https://github.com"),
#     gevent.spawn(f,"http://www.qfsf0220.top")]
# )


a=['中海瀛台','徐汇臻园','徐汇华园','枫桦景苑']
b=[gevent.spawn(f2,"http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw="+x) for x in a]
print(b)

gevent.joinall(b)