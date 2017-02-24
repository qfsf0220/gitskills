import  urllib
import  http.cookiejar
import  urllib.request
import  urllib.parse

url = "http://www.qfsf0220.top/auth/login"

postdata = urllib.parse.urlencode(
    {
        "email":"test2@qq.com",
        "passwd":"1234qwer"
    }
).encode("utf-8")

header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
"Host":"c.highpin.cn",
"Referer":"http://c.highpin.cn/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}

req = urllib.request.Request(url,postdata,header)

cookie = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

r=opener.open(req)

result = r.read().decode('unicode-escape')
print(eval(result)["msg"])  #可以通过eval函数转换成dict格式 ,变量不支持eval
import  sys
print(sys.getdefaultencoding())

