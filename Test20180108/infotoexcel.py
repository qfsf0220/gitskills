#-*- coding:utf-8 -*-
import asyncio
import aiohttp
from pyquery import  PyQuery as pq
import requests
import xlsxwriter

s=requests.session()

url="http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=020000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E8%BF%90%E7%BB%B4&keywordtype=2&curr_page=66&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9"

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           "Cookie":"guid=1515576263216090099; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60020000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%D4%CB%CE%AC%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1515576273%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1515576268%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D",
           "Host": "search.51job.com" ,
           "Origin": "http://search.51job.com"}


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            aa=(await resp.text(encoding='gbk'))
            print("*******"*300)
            # aa.encoding="gbk"
            # a_0=aa.text
            ddtile = pq(aa)
            jobname = ddtile(".cn").text()
            print(jobname)
            joborder = ddtile(" .t1").text()
            jobask = ddtile(".tBorderTop_box .bmsg.job_msg.inbox  ").text()
            # jobaddress = ddtile('.tCompany_main .fp').text()
            jobaddress = ddtile('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(3) > div > p').text()
            # print(jobname+'\n'+joborder+'\n'+jobask+'\n'+jobaddress)

            dicttest = {}
            jobname = re.split(r'[\s]', jobname)
            while '' in jobname:
                jobname.remove('')
            dicttest["职位"] = jobname[0]
            dicttest["地区"] = jobname[1]
            if '/月' in jobname[2]:
                dicttest["薪酬"] = jobname[2]
            else:
                dicttest["薪酬"]="请面谈"
            dicttest["公司名字"] = jobname[3]
            dicttest["公司性质"] = jobname[5]
            dicttest["公司规模"] = jobname[7]
            # dicttest["公司类别"] = jobname[9]
            dicttest["公司地址"] = jobaddress
            if len(joborder.split(' '))==3:
                dicttest["工作经验"] = joborder.split(' ')[0]
                dicttest["招聘人数"] = joborder.split(' ')[1]
                dicttest["发布时间"] = joborder.split(' ')[2]
            else:
                dicttest["工作经验"] = joborder.split(' ')[0]
                dicttest["招聘人数"] = joborder.split(' ')[2]
                dicttest["发布时间"] = joborder.split(' ')[3]
            dicttest["岗位职责"] = jobask
            print(dicttest)
            infolist.append(dicttest)
infolist=[]

for i in range(1,2):
    url="http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=020000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E8%BF%90%E7%BB%B4&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9".format(i)
    s.post(url,headers=headers)

    file = s.get(url)
    file.encoding='gbk'
    pagetext = file.text
    # print(pagetext)
    d=pq(pagetext)
    a1=d('#resultList .el:gt(1) ').text()
    a2=d('div.dw_table  [href$="0"][title][target]')
    a3=str(a2)

    import re
    a= re.findall(r'http://.*t=0',a3)
    a.pop(0)
    print(a)

    loop = asyncio.new_event_loop()
    tasks =[get("%s" % x)  for x in a]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

print("#############"*666)
print(infolist)

workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet()
a=0;b=0;c=0
for i in infolist[0].keys():
    worksheet.write(a,b,i)
    b+=1

# worksheet.write('A1',"aaaaaaaaa")
for a,b in enumerate(infolist):
    for  c in   range(len(b.values())):
        worksheet.write(a+1, c,list(b.values())[c])
        c+=1

workbook.close()