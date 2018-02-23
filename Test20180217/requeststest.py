import requests

response = requests.get("http://baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

response2 = requests.get("http://httpbin.org/get?name=gg&age=22")
data={"qq":'qq'}
response22 = requests.get("http://httpbin.org/get",params=data)#效果等同于 response2
print(response2.text)
##解析json
response3 = requests.get("http://httpbin.org/get")
#等于import  json json.loads(response3.text)
print(response3.text)
print(response3.json())
##获取二进制
response4 = requests.get("https://github.com/favicon.ico")
print(type(response4.text),type(response4.content))
#response4.content 是bytes 类型的  字节流
#保存字节流为文件
with open("githib.ico",'wb') as f:
    f.write(response4.content)
    f.close()
#post方法
response5 = requests.post("http://httpbin.org/post",data={"qq":"123"},headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"})
print(response5.json())
print("**"*20)
print(response5.status_code)
print(response5.headers)
print(response5.cookies)
print(response5.url)
print(response5.history)
#http code test
# response6= requests.get("http://qq.com/nima.html")
# exit() if not response6.status_code == requests.codes.not_found else print("404")
# exit() if not response6.status_code == 404 else print("404") #同上
##file 上传
file = {"file":open("githib.ico","rb")}
response7 = requests.post("http://httpbin.org/post",files=file)
print(response7.text)

###get cookie
response8 = requests.get("https://www.baidu.com")
print(response8.cookies)
for a,b in response8.cookies.items():
    print(a+"~~~~"+b)

## 会话维持  主要为了模拟登陆
s= requests.session()
s.get("http://httpbin.org/cookies/set/aaa/1234bb56789")
req_get_ck = s.get("http://httpbin.org/cookies")
print(req_get_ck.text)

print("“###证书验证")
# reqto12306 = requests.get("https://www.12306.cn") #这里 如果12306的证书不通过浏览器验证通过。所以直接报sslError错退出
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
reqto12306_2 = requests.get("https://www.12306.cn",verify=False)#verify 跳过验证，但是仍然会有一个warning 提示不安全
#需要在上面添加上disable_warning 来自于 requests.packages.urllib3包
print(reqto12306_2.status_code)

##代理设置
proxies={"http":"socks5://127.0.0.1:1080"}#socks 代理
# proxies={"http":"http://user:passwd@127.0.0.1:1080"} # http代理
response9= requests.get("http://httpbin.org/get",proxies=proxies)
print(response9.text)







