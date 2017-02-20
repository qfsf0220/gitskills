from   gevent import monkey;
from gevent import sleep
monkey.patch_all();
import  gevent
import requests
import  re,time
from pyquery import PyQuery as pq
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/47.0.2526.80 Safari/537.36"}
result_list=[]

def f2(url):
    # print("GET -> %s" % url)
    resp = requests.get(url,verify=True,headers=headers)
    data = resp.text
    # print("%s bytes recived from %s" %(data,url))
    d = pq(data)
    b=d('.comm-price').text()
    print(b)
    result_list.append(b)

a=['中海瀛台','徐汇臻园','徐汇华园','枫桦景苑']
b=['徐汇臻园','东湾度假村','苑宏新村','中海瀛台','徐汇苑',
   '南方新村','盛华景苑','徐汇华园','紫阳花园','印象欧洲',
   '浦润苑','华唐苑','银泰苑','新凯家园一期','中冶锦城',
   '漓江山水花园','华泾绿苑','华泾五村','华欣家园','东湾小区',
   '馨宁公寓','徐汇新干线','爱庐世纪新苑','新弘国际城','南方城',
   '晶欣坊','华发小区','枫桦景苑','华建一街坊','华沁家园','长桥一村','长桥五村']
c=['浦润苑','银泰苑','中冶锦城',
   '漓江山水花园','东湾小区','馨宁公寓','徐汇新干线','爱庐世纪新苑','新弘国际城','南方城',
   '晶欣坊','华发小区','枫桦景苑','华建一街坊','华沁家园','长桥一村','长桥五村']
t1 = time.time()


b=[gevent.spawn(f2,"http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw="+x) for x in c ]

gevent.joinall(b)
print(result_list,len(result_list))

c=sorted(result_list,key=lambda x:re.sub('\D', '',x))
d= map(lambda x:re.sub('(（(.*)\))','', x),c)
e= [x for x  in d if x !=""]

# def greenprint(ssttrr):
#     return ('\033[0;32;40m%s\033[0m' % ssttrr)
# def redprint(ssttrr):
#     return ('\033[0;31;40m%s\033[0m' % ssttrr)
# def yellowprint(ssttrr):
#     return ('\033[0;33;40m%s\033[0m' % ssttrr)
#
# for i in e :
#     if '↑' in re.split('\s+',i)[5] and i !="":
#         print(re.split('\s+',i)[0]+ " 本月"+yellowprint(re.split('\s+',i)[2].split('元')[0])+"元/平方米 , 比上月 " +redprint(re.split('\s+',i)[5]))
#     else:
#         print(re.split('\s+', i)[0] + " 本月" + yellowprint(re.split('\s+', i)[2].split('元')[0]) + "元/平方米 , 比上月 " + greenprint(re.split('\s+', i)[5]))
# t2 = time.time()
# print("用了 %.2f s" % (t2 - t1))