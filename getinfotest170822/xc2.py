#!/usr/bin/env python
# -*- coding:utf8 -*-
#
import datetime
import requests
from pyquery import PyQuery as pq
import json
import re

headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'GUID=09031059311076039565; _abtest_userid=681c682c-79ac-44d3-9740-ffc85673069f; cticket=391F551D43C95EFDD8F145099B2FD5C9F7051C1F6846EB03032BD549F0458174; DUID=u=72519CC6DF52552D2712B45217F210A8&v=0; IsNonUser=T; fplus_abtest_swift=M%3A36%2C170320_fld_newsf%3AE%3B; HotelCityID=43split%E4%B8%89%E4%BA%9AsplitSanyasplit2017-8-22split2017-08-23split0; DomesticUserHostCity=SHA|%c9%cf%ba%a3; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1503976659428; appFloatCnt=4; manualclose=1; FD_SearchHistorty={"type":"S","data":"S%24%u4E0A%u6D77%28SHA%29%24SHA%242017-08-25%24%u4E09%u4E9A%28SYX%29%24SYX"}; _bfa=1.1503298749016.1feze7i.1.1503366580829.1503371623703.4.26.10320605177; page_time=1503366875996%2C1503368127453%2C1503368127819%2C1503368977963%2C1503368978160%2C1503368999848%2C1503369000064%2C1503369020853%2C1503369021139%2C1503369116299%2C1503369116453%2C1503369142365%2C1503369142785%2C1503371625249%2C1503371633460%2C1503371633699%2C1503371857402%2C1503371880969%2C1503371881123%2C1503373677579%2C1503373677889%2C1503373700491%2C1503373700717%2C1503373713478%2C1503373713706; _RF1=140.207.146.122; _RSG=BOq.EcR40YCuzm9RwAnsdB; _RGUID=c88011b9-8efb-460b-b9f6-c4ae9b270f78; _ga=GA1.2.914799508.1503298751; _gid=GA1.2.1538991029.1503298751; _jzqco=%7C%7C%7C%7C%7C1.320692184.1503298749919.1503373702820.1503373715781.1503373702820.1503373715781.0.0.0.23.23; __zpspc=9.4.1503371859.1503373715.5%232%7Cwww.baidu.com%7C%7C%7C%7C%23; MKT_Pagesource=PC; _bfi=p1%3D101027%26p2%3D10320662761%26v1%3D26%26v2%3D25',
        'Host':'flights.ctrip.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }

s=requests.Session()

#mainurl='http://flights.ctrip.com/domestic/booking/SHA-SYX---D-adu-1/?dayoffset=35&ddate1=2017-09-25&ddate2=2017-09-30'
import sys
timetogo = sys.argv[1]
timetoback = sys.argv[2]
gourl='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=SHA&ACity1=SYX&SearchType=S&DDate1=%s&HasChild=T&IsNearAirportRecommond=0&LogToken=372053bf48b346b594e8f7ef96491429&rk=1.5327261863854047142908&CK=F4CDA1EFCD3ADD2F0ABF5F1BD17EC6BC&r=0.3110000010502681380010' % (timetogo)

backurl='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=SYX&ACity1=SHA&SearchType=S&DDate1=%s&HasChild=T&IsNearAirportRecommond=0&LogToken=372053bf48b346b594e8f7ef96491429&rk=1.5327261863854047142908&CK=F4CDA1EFCD3ADD2F0ABF5F1BD17EC6BC&r=0.3110000010502681380010' % (timetoback)

ab= s.get(gourl,headers=headers)
#d=pq(ab.text)
result =  ab.text
dictr = json.loads(result)

ab2 = s.get(backurl,headers=headers)
result2 = ab2.text
dictr2 =json .loads(result2)
#file =open('/tmp/1234.txt','w')
#file.write(str(dictr['fis'][0]['dpbn']))
#file.close()
def info(a):
    quchufa= (dictr['fis'][a]['dpbn'])
    qumudi= (dictr['fis'][a]['apbn'])
    quprice= (dictr['fis'][a]['lp'])
    qudaodatime=(dictr['fis'][a]['at'])
    quchufatime=(dictr['fis'][a]['dt'])
    quhangban= (dictr['fis'][a]['fn'])
    qupricechild= (dictr['fis'][a]['scs'][2]['chip'])

#    huichufa= (dictr2['fis'][a]['dpbn'])
#    huimudi= (dictr2['fis'][a]['apbn'])
#    huiprice= (dictr2['fis'][a]['lp'])
#    huidaodatime=(dictr2['fis'][a]['at'])
#    huichufatime=(dictr2['fis'][a]['dt'])
#    huihangban= (dictr2['fis'][a]['fn'])
#    huipricechild= (dictr2['fis'][a]['scs'][2]['chip'])
#    return ('出发地:'+quchufa+'\t\t'+huichufa+'\n'+'出发时间:'+quchufatime+'\t'+huichufatime+'\n'+'目的地:'+qumudi+'\t\t'+huimudi+'\n'+ '抵达时间:'+qudaodatime+'\t'+huidaodatime+'\n'+'价格:'+str(quprice)+'\t\t\t'+str(huiprice)+'\n'+ '儿童价格:'+str(qupricechild)+'\t\t'+str(huipricechild)+'\n'  +'航班号:'+quhangban+'\t\t\t'+huihangban+'\n----------------------------------------------')
    return ('出发地:'+quchufa+'\t\t'+'\n'+'出发时间:'+quchufatime+'\t'+'\n'+'目的地:'+qumudi+'\t\t'+'\n'+ '抵达时间:'+qudaodatime+'\t'+'\n'+'价格:'+str(quprice)+'\t\t\t'+'\n'+ '儿童价格:'+str(qupricechild)+'\t\t'+'\n'  +'航班号:'+quhangban+'\t\t\t'+'\n')

def info2(a):
    huichufa= (dictr2['fis'][a]['dpbn'])
    huimudi= (dictr2['fis'][a]['apbn'])
    huiprice= (dictr2['fis'][a]['lp'])
    huidaodatime=(dictr2['fis'][a]['at'])
    huichufatime=(dictr2['fis'][a]['dt'])
    huihangban= (dictr2['fis'][a]['fn'])
    huipricechild= (dictr2['fis'][a]['scs'][2]['chip'])
    return ('出发地:'+huichufa+'\t\t'+'\n'+'出发时间:'+huichufatime+'\t'+'\n'+'目的地:'+huimudi+'\t\t'+'\n'+ '抵达时间:'+huidaodatime+'\t'+'\n'+'价格:'+str(huiprice)+'\t\t\t'+'\n'+ '儿童价格:'+str(huipricechild)+'\t\t'+'\n'  +'航班号:'+huihangban+'\t\t\t'+'\n')

infolist=[]
infolist2=[]
for i in range(len(dictr['fis'])):
    infolist.append(info(i))
    infolist2.append(info2(i))
sortinfo =sorted(infolist,key=lambda x :int(re.search(r'.*价格:(\d+).*',x).group(1)))
sortinfo2 =sorted(infolist2,key=lambda x :int(re.search(r'.*价格:(\d+).*',x).group(1)))

zz=list(zip(sortinfo,sortinfo2))

file =open('/tmp/1234.txt','w')
file.write(str(zz))
file.close()



for i in zz:
    print(   i[0].split('\n')[0]+'\t\t'+i[1].split('\n')[0]     )
    print(   i[0].split('\n')[1]+'\t\t'+i[1].split('\n')[1]     )
    print(   i[0].split('\n')[2]+'\t\t'+i[1].split('\n')[2]     )
    print(   i[0].split('\n')[3]+'\t\t'+i[1].split('\n')[3])
    print(   i[0].split('\n')[4]+'\t\t'+i[1].split('\n')[4]     )
    print(   i[0].split('\n')[5]+'\t'+i[1].split('\n')[5]     )
    print(   i[0].split('\n')[6]+'\t\t'+i[1].split('\n')[6]     )
    print('**'*30)

#for i in sortinfo:
#    print(i)
#print("*" *100)
#for i in sortinfo2:
#    print(i)

#now =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')