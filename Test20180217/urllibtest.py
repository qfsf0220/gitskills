import urllib.request
import sys,io
print(sys.version_info)
print(sys.getdefaultencoding())
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#win7 默认终端编码是gb18030 （还有gbk 和gb2312。）
url = "http://www.baidu.com"

##############urllib 的request 方法使用。########
#GET 方式获取网页
rep = urllib.request.urlopen(url)
print(rep.read().decode("utf-8"))#reponse的read方法获得的是bytes 字节流 byte 转 string 需要 decode  string 转成byte 用encode
#POST 方式
import urllib.parse
import urllib.request
data_test = bytes(urllib.parse.urlencode({"name":"qqq"}),encoding="utf-8") #post 发送一个data  字典{name qqq}
rep = urllib.request.urlopen("http://httpbin.org/post",data=data_test)
print(rep.read())
### 超时2秒等待
rep2 = urllib.request.urlopen("http://httpbin.org/get",timeout=2)
print(rep2.read())
### 测试超时错误，如果连接使用超过0.1秒 报URLerror 的错
import socket
import urllib.error

try:
    rep3 = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
except urllib.error.URLError as a:
    if isinstance(a.reason,socket.timeout):
        print("time out ...")
print(socket.timeout)
print(type(socket.timeout))
### request info
rep4 = urllib.request.urlopen("https://www.python.org")
print(rep4.status)
print(rep4.getheaders())
print(rep4.getheader("Content-Type"))
###request 方法2
request = urllib.request.Request("https://python.org")
req5 = urllib.request.urlopen(request) #完全等同于 urllib.request.urllopen("https://pytho.org")
print(req5.read().decode("utf-8"))
###添加请求头
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Host":"httpbin.org"
}
dicttest = {"name":"sdasd"} #这里 可以直接写成 b'name=sdasd'的字节形式 传给urlopen的data使用

data_test2 =bytes(urllib.parse.urlencode(dicttest),encoding="utf-8")#urllib.parse.urlencode 把字典转换为url格式 最后转成字节 作为data
res6 = urllib.request.Request("http://httpbin.org/post",data=data_test2,headers=headers,method="POST")
##headers=xxx 也可以不写 用res6.add_header("User-Agent","Mozxxxxxxx") （元组） 来实现
req6 = urllib.request.urlopen(res6)
print(req6.read().decode("utf-8"))
print(data_test2)

###代理
# proxy_handler = urllib.request.ProxyHandler({
#     "http://xxxx.com:8888"
# })
# opener = urllib.request.build_opener(proxy_handler)
# req7 = opener.open("http://www.ww.com")
# print(req7.read())

#### ##cookie
##获取cookie信息
import  http.cookiejar
cookie= http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
reponse = opener.open("http://www.baidu.com")
for i in cookie:
    print(i.name + " = "+ i.value)
##保存coockie信息为文本来复用
filename = "cookie.txt"
ck=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(ck)
opener =urllib.request.build_opener(handler)
req7 = opener.open("http://qq.com")
ck.save(ignore_discard=True,ignore_expires=True)
