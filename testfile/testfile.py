import requests

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/47.0.2526.80 Safari/537.36"}

url = 'http://www.qianfanedu.cn/portal.php'
resp = requests.get(url,verify=True,headers=headers)

print(resp.text)