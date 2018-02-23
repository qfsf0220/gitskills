import  requests
import time
# data = {
# 'what':'show',
# 'page':'2',
# 'pageSize':'',
# 'api':'x/search',
# }
data= {
'cateId':"1",
'status':1
}
headers={"authority":"try.taobao.com",
"method":"POST",
"path":"/api3/call?what=show&page=2&pageSize&api=x%2Fsearch",
"scheme":"https",
"accept":"application/json, text/javascript, */*; q=0.01",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
"content-length":"23",
"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
"cookie":"t=9abe1346a3d2a615d1ece5475411a232; cna=mgYDE8rG+TUCAYzOSNLrtmzo; enc=PohC3k%2Fl3e1Xp5Ve47FkyW%2B0l%2Fwih4Rx7TkfkKSwGZAOGsX0KiQHmmN5yURKFMkKEFuoEboRFWOqgC8DvPJn%2BA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _tb_token_=ZGHSMeF9iLbYFmc51XPO; isg=BF9fYxtIeZg4TX11W9-uX0wf7rNF1PZFdXgR2vGs-45VgH8C-ZRDtt3WRhD-GIve",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
"origin":"https://try.taobao.com",
"referer":"https://try.taobao.com/",
"x-csrf-token":"ZGHSMeF9iLbYFmc51XPO",
"x-requested-with":"XMLHttpRequest"}


a= requests.post("https://try.taobao.com/api3/call?what=show&page=2&pageSize&api=x%2Fsearch",data=data,headers=headers)
print(a.url)
test = a.text
import  json
aaa = json.loads(test)
for i in (aaa['result']['items']):
    print('商品:'+i['title'] +"\t\t\t申请人数:"+str(i['requestNum'])+"\t价格:"+str(i['price'])+"\t截止时间:"+time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(i['endTime']/1000)))


