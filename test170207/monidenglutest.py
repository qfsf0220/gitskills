#-*- codeing:utf8 -*-
import urllib.request
import urllib.parse
import urllib
import  re
# data =urllib.urlencode(values)
url = 'http://www.qfsf0220.top/auth/login'

headers = (
'User-Agent',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 \
(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

def login():
    username="qfsf0220@qq.com"
    password= "1234qwer"
    data = {
        "email": username,
            "passwd": password}

    postdata = urllib.parse.urlencode(data).encode(encoding='UTF8')
    try:
        request = urllib.request.Request(url,postdata)
        repose = urllib.request.urlopen(request)
        text = repose.read().decode('utf-8')
        # text = text.split(':')
        text2=re.split(':',str(text))
        a=((re.sub('"|}','',text2[2])))
        a.encode('utf8').decode('utf8')

        print(a)

        print(text)
        print(type(a))
        print(type(text))
    except Exception as e:
        print("error...")
        print(e)


if __name__ == '__main__':
    login()

