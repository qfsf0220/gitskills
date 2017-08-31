'''
http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=ZM7IU68NTP&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=%E5%85%B6%E4%BB%96

http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=OZTBSUCD1Z&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=%E5%85%B6%E4%BB%96

'''

"""

http://c.ndkey.com/amcloud/page/portal_redirect/index.html

"""
#!/usr/bin/env python
# -*- coding:utf8 -*-
#
import datetime
import requests
from pyquery import PyQuery as pq

headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }

url = 'http://c.ndkey.com/amcloud/page/portal_redirect/index.html'
url2= "http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=OZTBSUCD1Z&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=%E5%85%B6%E4%BB%96"#amExtraParams: {}  tenantType: 其他
s=requests.Session()

#query String parameters    handlerId=403bc60f-da0f-44b2-b50c-8d5b46a4cfd6&sessionId=0e08f432-8d65-11e7-9385-009027ef0f2c&terminalIp=172.16.69.35&terminalMac=9c%3A5c%3A8e%3A70%3A07%3A4d
#http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=ZM7IU68NTP&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=%E5%85%B6%E4%BB%96
#http://172.16.96.100:8080/am/controller/portal/login

#http://172.16.96.100:8080/am/controller/portal/navigation/next/go?currentStage=2

x= """ handlerId:403bc60f-da0f-44b2-b50c-8d5b46a4cfd6
sessionId:0e08f432-8d65-11e7-9385-009027ef0f2c
terminalIp:172.16.69.35
terminalMac:9c:5c:8e:70:07:4d
-----------
handlerId:403bc60f-da0f-44b2-b50c-8d5b46a4cfd6
sessionId:0e08f432-8d65-11e7-9385-009027ef0f2c
terminalIp:172.16.69.35
terminalMac:9c%3A5c%3A8e%3A70%3A07%3A4d

<input name="username" class="text" id="un-userName" style="width:100%;">
<input type="password" name="password" class="text" id="un-password" style="width:100%;">
<a id="un-login" i18n-key="login">登录</a>
"""

posturl = "http://172.16.96.100:8080/am/controller/portal/userPassword/passwordRequirement"

postdata ="POST   data = {'loginName':'f......'}"


r=s.get(url,headers=headers)

rtext = pq(r.text)
print(r.text)





