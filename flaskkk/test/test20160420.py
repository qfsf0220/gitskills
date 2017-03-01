# -*- coding: utf-8 -*-
import os,re
import  requests
import chardet
import json
import sys


# sys.setdefaultenconding('utf-8')
#
# a="xxaaxxbbxxccxx"
#
# b= re.findall('xx(.*?)xx',a)
# c=[]
# for i in b:
#     c.append(i)
#
# print reduce(lambda x,y:x+y,c)
#
# s='''
#     aaxxbb
#     xxccxxddxx
# '''
# d=re.findall(r'xx(.*?)xx',s,re.S)  #re.S 加上以后支持匹配\n这样的换行符
# print d

#
#
# s2='aaxxbbxxccxxddxxee'
#
# e=re.search('xx(.*?)xx.*xx(.*?)xx',s2).group(1)
# print (e)
#
# e2=re.findall('xx(.*?)xx.*xx(.*?)xx',s2)
# print (e2)[0][0]
#
# sub3=re.sub('xx(.*?)xx','xx%sXX'%'--',s2)
# print sub3
#
#
# s3="qq1234qfsf"
# n1=re.findall('(\d+)',s3)
# print n1



# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
# html=requests.get("http://xmdswiki.opd2c.com/index.php?r=cards%2Findex&level=6", headers=header)
# html.encode='utf-8'
# htmlpage=html.text
# # print htmlpage
# picurl=re.findall(r'<img src="(.*.png)',htmlpage)
# picfullurl=map(lambda x:'http://xmdswiki.opd2c.com/'+x,picurl)
# # for i in picurl:
# #     print 'http://xmdswiki.opd2c.com/'+i
# name=re.findall(r'\.png" alt="(.*?)"',htmlpage,re.S)
# for i in range(len(name)):
#     print picfullurl[i],name[i]

#
# a=['a','b','c','d']
# b=[5,6,7,8,9]
# c=zip(a,b)
# for i in c:
#     print i[0],str(i[1])
# if not c:
#     print "ok"
# else:
# #     print "oookkk"
# c=zip(a,b)
#
# for a,b in c:
#     print a,b

# try:
#     for i in range(len(b)):
#         print a[i],b[i]
# except IndexError,error:
#     pass
#

# for i in range(len(b)):
#     if len(a)>i:
#         print a[i],b[i]
#     else:
#         break

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
#
#
# html=requests.get("http://club.pchome.net/forum_1_15.html", headers=header)
# html.encode='utf-8'
# htmlpage=html.text
# # print htmlpage
# kdsurl=re.findall(r'<span class.*?title="(.*?)">',htmlpage,re.S)
# print htmlpage
# for i in kdsurl:
#     print i


# xxx='<span class="n3"><a rel="http://club-img.kdslife.com/attach/1k0/bm/4r/o1nocs-1l8u.jpg@0e_0o_1l_128h_128w_90q.src" href="/thread_1_15_8713021__.html" title="[iPhone]高品质xs 九分半。">[iPhone]高品质xs 九分半。</a>(<A HREF=thread_1_15_8713021_1_.html class=zhuti>1</A>&nbsp;<A HREF=thread_1_15_8713021_2_.html class=zhuti>2</A>&nbsp;<A HREF=thread_1_15_8713021_3_.html class=zhuti>3</A>..<A HREF=thread_1_15_8713021_9_.html class=zhuti>9</A>)<img src="http://img.club.pchome.net/html/icons/dv.gif"><img src="http://img.club.pchome.net/html/icons/iphone.png" title="该帖发自手机宽带山 m.kdslife.com"></span>'
#
# g=re.findall(r'<span class.*?title="(.*?)">',xxx,re.S)
#
# print g[0]

# a="xxaaxxbbxxccxx"  #test...
#
#
# print re.search(r'xx(.*?)xx',a).groups()


# url='http://www.baidu.com/b'
# # F12  form data 的数据提交  这个一本是数据异步加载网站才需要的。
# datapost={
#     'entities_only':'true'   #注意 true 和1  都是  string
#     'page':'1'
# }
# html_post = requests.post(url,data=datapost)
# title = re.findall('"card-title">(.*?)</div>',html_post.text,re.S)
# for i in title:
#     print i

from lxml import etree
###
#xpath  提取内容    //定位根节点   /往下层    提取文本内容：/text()  提取属性内容: /@href /@title 等等
#selector = etree.HTML(page_html_text)
#content = selector.xpath('//body/div[@id="qq"]/li/text()')
#提取的是列表 需要 for 循环打印 或者 print[x] 输出元素
#xpath 特殊用法
#content =selector.xpath('//div[start-with(@id,"test")]/text()')
#对于复杂页面的话 可以继续遵从 先达后小的原则
#
#data=selector.xpath('//div[@id="test3"]')[0] #吧div id是3的内容全部提取
#info =data.xpath('string(.)')  #提取所有的字符串
#content2 =info.replace('\n','').replace(' ','')  #把\n 和 空格都换成空
#print content2
#
###

from multiprocessing.dummy import Pool as PPP
# import  requests,time
# class okok:
#     def getsource(self,url):
#         html=requests.get(url).text
#         print "load ok!"
# gg=okok()
#
#
# urls=[]
# for i in  range(0,550,50):
#     newpage="http://tieba.baidu.com/f?kw=消灭都市官方&ie=utf-8&pn="+str(i)
#     urls.append(newpage)
    # print newpage
# time1=time.time()
# for i in urls:
#     # print i
#     gg.getsource(i)
# time2=time.time()
# print u'单线程' +str(time2-time1)

# pool=PPP(4)
# time3=time.time()
# reslut=pool.map(gg.getsource,urls)
# pool.close()
# pool.join()
# time4=time.time()
# print u'多线程'+str(time4-time3)
# # selector = etree.HTML(page_html_text)
#
# def towrite(contentdict):
#     f.writelines('回帖时间'+str(contentdict['topic_reply_time'])+'\n')
#     f.writelines('回帖内容' + str(contentdict['topic_reply_content']) + '\n')
#     f.writelines('回帖人' + str(contentdict['user_name']) + '\n')
#
# def spider(url):
#     html=requests.get(url)
#     selector = etree.HTML(html.text)
#     content_field=



#
# a='setdit=1; Hm_lvt_e8499b7329e8d5d44f3f4c8902bb043a=1461313932,1461313936; Hm_lpvt_e8499b7329e8d5d44f3f4c8902bb043a=1461313936; __userId=548980164; sessionID=7fc41cf9f546641b9f23834da50c69c6; __P_NickName=Arking; __P_JS_NickName=Arking; __P_UserName=shenhuide; __P_UserId=548980164; __P_AuthCode=3f4ca3811c8136bab3086759d3caf25d'
# b="z_pro_city=s_provice%3Dshanghai%26s_city%3Dshanghai; lastLoginTime=1461304378; lastLoginIp=100.109.1.27; __P_AuthCode=3f4ca3811c8136bab3086759d3caf25d; __userId=548980164; sessionID=5908e9aca4163d3215b535e88781aacb; __P_NickName=Arking; __P_JS_NickName=Arking; __P_UserName=shenhuide; __P_UserId=548980164; Hm_lvt_e8499b7329e8d5d44f3f4c8902bb043a=1461304339,1461304380,1461304623; Hm_lpvt_e8499b7329e8d5d44f3f4c8902bb043a=1461304623; setdit=1"
# c="z_pro_city=s_provice%3Dshanghai%26s_city%3Dshanghai; lastLoginTime=1461307833; lastLoginIp=100.109.1.9; __P_AuthCode=3f4ca3811c8136bab3086759d3caf25d; __userId=548980164; sessionID=d50574b3a21084baf49e4ce255d155d5; __P_NickName=Arking; __P_JS_NickName=Arking; __P_UserName=shenhuide; __P_UserId=548980164; Hm_lvt_e8499b7329e8d5d44f3f4c8902bb043a=1461304910,1461304946,1461307837,1461308371; Hm_lpvt_e8499b7329e8d5d44f3f4c8902bb043a=1461308371; setdit=1"
# d="setdit=1; Hm_lvt_e8499b7329e8d5d44f3f4c8902bb043a=1461303978,1461304064,1461305980,1461305990; Hm_lpvt_e8499b7329e8d5d44f3f4c8902bb043a=1461308575; lastLoginTime=1461308403; lastLoginIp=100.109.1.13; __userId=548980164; sessionID=6c9dad5b83b61a67130e8df88bf46e37; __P_NickName=Arking; __P_JS_NickName=Arking; __P_UserName=shenhuide; __P_UserId=548980164; __P_AuthCode=3f4ca3811c8136bab3086759d3caf25d"
# cook = {"Cookies":"a"}
#
# urlxx = "http://passport.pchome.net/login.php?action=login&goto=http://club.pchome.net/forum_1_15.html"
# url ="http://club.pchome.net/forum_1_15.html"
#
# html= requests.get(url,cookies=cook).text
# print html



from bs4 import BeautifulSoup


loginpage="http://passport.pchome.net/login.php"
userpage="http://my.pchome.net/self/"
data={
    "username":"shenhuide",
    "password":"1234qwer"
}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
    "Referer": "http://www.kdslife.com/forum_1_15.html"

}

s=requests.Session()
r=s.post(loginpage,data=data,headers=headers)
okpage=s.get(userpage)
data=BeautifulSoup(okpage.content,"lxml")
text=data.find_all("li",attrs={"class":re.compile('td.*')})
for i in text:
    print i.get_text()
