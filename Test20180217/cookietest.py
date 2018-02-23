import requests
res = requests.get("https://www.baidu.com")
print(res.cookies)
for a,b in res.cookies.items():
    print(a+"  "+b)