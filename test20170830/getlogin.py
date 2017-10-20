#!/usr/bin/env python
# -*- coding:utf8 -*-
#
import datetime
import requests
from pyquery import PyQuery as pq

headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        ,'Cookie':'languageValue=zh;DKEYJSESSIONID=39138C6DBB4232F6B4469C4D46F5AFDF'}

s=requests.Session()

s.get("http://www.163.com",headers=headers)
#
# r=s.get("http://172.16.96.100:8080/am/controller/portal/qrCodeGuest/qrCodeImage",headers=headers)
#
# print (r.text)
# print(s.get("http://c.ndkey.com/amcloud/page/portal_redirect/index.html",headers=headers).text)

postrequirement="http://172.16.96.100:8080/am/controller/portal/userPassword/passwordRequirement"
postreqdata={"loginName" : "feng.qian"}
r1=s.post(postrequirement,data=postreqdata,headers=headers)

postlogin = "http://172.16.96.100:8080/am/controller/portal/userPassword/login"
postdata ={'loginName':'feng.qian',"password":"Gjk_123456","dynamicPassword":""}
r2=s.post(postlogin,data=postdata,headers=headers)

getcurrentstage=s.get("http://172.16.96.100:8080/am/controller/portal/navigation/next/go?currentStage=2",headers=headers)
print(getcurrentstage.text)

print("111"*20)

getlogin= s.get("http://172.16.96.100:8080/am/controller/portal/login",headers=headers)
print(getlogin.text)

print("222"*20)

getsuccess = s.get("http://172.16.96.100:8080/am/controller/portal/navigation/success",headers=headers)
print(getsuccess)
print("333"*20)

posturl3= "http://172.16.96.210:9090/identity/terminalPortal";
postdata3={"cmd":"login","handlerId":"403bc60f-da0f-44b2-b50c-8d5b46a4cfd6","loginName":"feng.qian-S-V3ZC0O2NOH","password":"KhPlYmNCyCGh","account":"feng.qian","nextUrl":"http://172.16.96.100:8080/am/controller/portal/navigation/success"}
r3 = s.post(posturl3,data=postdata3,headers=headers)
#
#
#
urlx="http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=true&language=zh-CN&portalSessionId=0QCZQLF23P&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%22terminalAutoLoginTimeout%22%3A%22430827%22%7D&portalType=87012f5e-1876-4bb9-8b63-5ee8179877f9&tenantType=%E5%85%B6%E4%BB%96&terminalMac=9C%3A5C%3A8E%3A70%3A07%3A4D&loginName=feng.qian&roles=_OPS_all_Technology_All-SH"
print( s.get(urlx,headers=headers).text)

print("444"*20)

print(s.get("http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=ZM7IU68NTP&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=其他",headers=headers).text)

#
#
# """
# http://c.ndkey.com/amcloud/page/portal_redirect/index.html
# """