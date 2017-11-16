import requests
from pyquery import PyQuery as pq
# from  multiprocessing import  Process,Pool
from functools import reduce

headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"aliyungf_tc=AQAAAKQUDUHpfQcA0kjOjPhX+bpgscKo; select_city=310000; cityCode=sh; lianjia_uuid=feb527ce-d515-45bd-a7ec-dfeb3ebc0021; gr_user_id=91dbe87c-d7ea-45a2-87aa-66ce0344cf33; _gat=1; _gat_u=1; _ga=GA1.2.2111075692.1510560992; ubt_load_interval_b=1510727097153; ubt_load_interval_c=1510727097153; lianjia_ssid=ac8b3630-d390-0b36-cf58-6ff0e3579417; ubta=2299869246.3514217314.1510560994903.1510727096345.1510727097221.4; ubtb=2299869246.3514217314.1510727097222.C71113FED8EAA327321AA5D6FA2D0529; ubtc=2299869246.3514217314.1510727097222.C71113FED8EAA327321AA5D6FA2D0529; ubtd=4; gr_session_id_970bc0baee7301fa=a10f82c0-102a-4d31-adf4-2e58eac6a64b",
"Host":"sh.lianjia.com",
"Referer":"http://sh.lianjia.com/",
"Upgrade-Insecure-Requests":"1" ,
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
houselist = ["徐汇华园","盛华景苑","南方新村","长桥一村","光华园","印象欧洲（公寓）","华泾绿苑","新凯家园","银泰苑","老总的高端小区","华欣家园","东湾小区","新弘国际城（公寓）","华滨家园","贫民窟"]
info_list=[]
def get(name):
    url= "http://sh.lianjia.com/ershoufang/rs%s" % name
    a = requests.get(url=url,headers=headers)
    try:
        num = pq(a.text)('.m-side-bar').text()
        a = num.split(' ')
        # houseinfo=(a[0]+": "+"\033[0;31m%s\033[0m"%a[7]+" 元每平米 正在出售:"+a[10]+"套" )
        houseinfo=(a[0]+": %s"%a[7]+" 元每平米 正在出售:"+a[10]+"套" )
        info_list.append(houseinfo)
    except IndexError  as e:
        info_list.append(name+": 这个小区可能不存在，请检查")
    except UnboundLocalError as e:
        info_list.append(name + ": 这个小区可能不存在，请检查")
    except ConnectionError as e:
        info_list.append("网站大概有问题")

from tkinter import *
def mylabel():
    s1 = e1.get()
    houselist.append(s1)
    print(houselist)
    for i in houselist:
        get(i)

    info_list_sorted = sorted(list(set(info_list)), key=lambda x: x.split(' ')[1])
    textprint =reduce(lambda x,y:x+'\n'+y,info_list_sorted)
    # s=Label(root,text=textprint)
    # s.pack(side=BOTTOM,expand=YES,fill=BOTH)

    if t:
        t.delete(1.0,END)
        t.insert(1.0, textprint)

root =Tk()
root.wm_title("简易房价查询")
root.geometry("320x400")

t = Text(root,width=10,height=10)
scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=BOTH)
t.pack(side=BOTTOM, expand=YES,fill=BOTH)
scroll.config(command=t.yview)
t.config(yscrollcommand=scroll.set)

w3 = Label(root,text="Powered by qf",relief="solid",borderwidth=1)
w3.pack(anchor=NE)
w1= Label(root,text="点击 \"查询\" 查看",background="pink")
w1.pack()

w2=Label(root,text="自定义小区名:")
w2.pack(side=TOP,fill=NONE)

e1=Entry(root)
e1.pack(anchor=CENTER)



b1 = Button(root,text="查询",command=mylabel)
b1.pack(anchor=CENTER)
w1.mainloop()


