import random
import string
import requests
from pyquery import PyQuery as pq
from collections import Counter
from pyecharts import  Bar

b = string.ascii_lowercase
x =[str(random.randint(0,9))+str(y) for x in range(10) for y in random.choice(b)]
nameandcss="""北京大学,#js_content > table:nth-child(6) > tbody > tr
清华大学,#js_content > table:nth-child(11)
北京交通大学,#js_content > table:nth-child(14) > tbody > tr
北京理工大学,#js_content > table:nth-child(18) > tbody > tr
北京中医药大学,#js_content > table:nth-child(22)
复旦大学,#js_content > table:nth-child(38) > tbody
交通大学,#js_content > table:nth-child(46)
华东理工大学,#js_content > table:nth-child(50)
东华大学,#js_content > table:nth-child(54)
华东师范大学,#js_content > table:nth-child(58)
上海外国语大学,#js_content > table:nth-child(62)
上海财经大学,#js_content > table:nth-child(66)
上海大学,#js_content > table:nth-child(70)"""

url= "https://mp.weixin.qq.com/s/_R038XjJRV0m35uOaImAiQ"
a=requests.get(url).text
doc=pq(a)

def get_dict(selector):
    bjdx_gaozhong=(doc(selector).text())
    bjdx_gaozhong_list_tmp = bjdx_gaozhong.split(' ')
    # print(bjdx_gaozhong_list)
    bjdx_gaozhong_list= [bjdx_gaozhong_list_tmp[x] for x in range(1,len(bjdx_gaozhong_list_tmp),2) ]
    if "毕业学校名称" in bjdx_gaozhong_list:
        bjdx_gaozhong_list.remove("毕业学校名称")
    bjdx_dict=(Counter(bjdx_gaozhong_list))
    # for i,j in bjdx_dict.items():
    #     print(i,j)
    return(bjdx_dict)

# for i in nameandcss.split('\n'):
#     print("****"*5,i.split(',')[0],"****"*5)
#     # get_dict(i.split(',')[1])
#     print(get_dict(i.split(',')[1]))

bj=(nameandcss.split('\n')[0].split(',')[1])
countbj=get_dict(bj)

attr_tmp=(get_dict(bj) .keys() )
attr = [x for x in attr_tmp]

qh=(nameandcss.split('\n')[1].split(',')[1])
countqh=get_dict(qh)

attr2_tmp=(get_dict(qh).keys())
attr2 = [x for x in attr2_tmp]

bingji=list(set(attr).union(set(attr2)))

chabj=[x for x in bingji if x not in attr]

chaqh = [x for x in bingji if x not in attr2]

attr_yes =set(chabj+chaqh+bingji)
attrok=sorted(attr_yes)
print(attrok)

for i in chabj:
    countbj.setdefault(i,0)
bjv=sorted(countbj.items(),key=lambda x:x[0])
print(bjv)

v1=[x[1] for x in bjv]
print(v1)


for i in chaqh:
    countqh.setdefault(i,0)
qhv=sorted(countqh.items(),key=lambda x:x[0])
print(qhv)

v2=[x[1] for x in qhv]
print(v2)


bar = Bar  ("清华北大（上海）自主选拔录取人数",height=650,width=1200)
bar.add("北京大学",attrok,v1,is_stack=True,xaxis_interval=0, xaxis_rotate=0, yaxis_rotate=0,xaxis_margin=2,is_xaxislabel_align=True,is_xaxis_boundarygap=True,xaxis_label_textsize=9,is_convert=True)
bar.add("清华大学",attrok,v2,is_stack=True,xaxis_interval=0, xaxis_rotate=0, yaxis_rotate=0,xaxis_margin=2,is_xaxislabel_align=True,is_xaxis_boundarygap=True,xaxis_label_textsize=9,is_convert=True)
bar.render()