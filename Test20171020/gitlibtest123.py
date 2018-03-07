import requests
from pyquery import PyQuery as pq
import time

# s= requests.session()
#
#
# headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#  'Accept-Encoding': 'gzip, deflate, sdch',
#  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#  'Cache-Control': 'max-age=0',
#  'Connection': 'keep-alive',
#  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#
# a =s.post('http://gitblit.sumscope.com:81/?wicket:interface=:0:userPanel:loginForm::IFormSubmitListener::',{'username':'qa-release','password':'123456',"id1_hf_0": "","wicket:bookmarkablePage": ":com.gitblit.wicket.pages.MyDashboardPage"},headers=headers)
#
# maintext = s.get("http://gitblit.sumscope.com:81/user/qa-release")
# # print(maintext.text)
# d= pq(maintext.text)
# allprojectlist= d('.repository').text().split(' ')
# print(allprojectlist)
# # url = "http://gitblit.sumscope.com:81/summary/~qa-release%2F{}.git".format (allprojectlist[0]  )
# url = "http://gitblit.sumscope.com:81/summary/~qa-release%2Fcdh_plus_realtime_connector_cfets_release.git"
# print(url)
# onepagetext = s.get(url).text
# # print(onepagetext)
#
# d2= pq(onepagetext)
#
# branchnodian = d2(".pretty .list.name").text()
#
# print(branchnodian)
#
# d22 = pq(onepagetext)
#
# branchyoudian = d22(".pretty .hidden-phone [href^='../commit']")
# import re
# aaaaa = re.findall(r'<a.*?git/(.*?)" class.*?',str(branchyoudian))
# print(aaaaa)


#  body > div:nth-child(4) > div:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(2) > span > a


#$("[href$='.jpg']")

import  os
import  stat

# flist =os.listdir("E:\\gitdocument\\cdh_plus_restfulapi_release")
# for i in flist:
#     if os.path.isdir("E:\\gitdocument\\cdh_plus_restfulapi_release"+"\\"+i):
#         print("is dir ")
#         flist.remove(i)
#     else:
#         print("file")
# flist = flist[-3:]
# print(flist)
# sortflist = flist.sort(key=lambda fn:os.path.getmtime( "E:\\gitdocument\\cdh_plus_restfulapi_release"+"\\" + fn))

path="E:\\gitdocument\\"
flist = os.listdir(path)
fileabspath = [x for x in flist if os.path.isdir(path+x) is True]

print(fileabspath)



for i in fileabspath:
    print("remove %s%s" % (path,i))
    # os.system('rd/s/q E:\\gitdocument\\%s' % (i))
    time.sleep(2)



# def del_file(path):
#     for i in flist:
#         path_file = os.path.join(path, i)
#         print(path_file)
#         if  os.path.isdir(path_fi
#
#             for j in os.listdir(path_file):
#                 if os.path.isfile(j):
#                     path_file_in_dic=os.path.join(path_file+"\\"+j)
#                     print(path_file_in_dic)
#                     os.remove(path_file_in_dic)
#                 else:
#                     # os.rmdir(path_file+"\\"+j)
#                     del_file(path_file)

# for i in fileabspath:
#     global rofile
#     rofile=path+i+"\\.git\\objects"
#     try:
#         for j in os.listdir(rofile):
#             rofilein = (rofile+"\\"+j)
#             for k in os.listdir(rofilein):
#                 print(rofilein+"\\"+k)
#                 os.chmod(rofilein+"\\"+k,stat.S_IWRITE)
#                 os.remove(rofilein+"\\"+k)
#     except FileNotFoundError as e:
#         print(e)
#
# import  shutil
# try:
#     shutil.rmtree(path)
# except PermissionError as e:
#     print(e)
# import  stat
# os.chmod('E:\\gitdocument\\cdh_plus_restfulapi_release\\.git\\objects\\pack\\pack-371e04b56b68b729b6cff8e8c52e3b325991e1dc.idx',stat.S_IWRITE)
# os.remove('E:\\gitdocument\\cdh_plus_restfulapi_release\\.git\\objects\\pack\\pack-371e04b56b68b729b6cff8e8c52e3b325991e1dc.idx')

# os.system('rd/s/q E:\\gitdocument\\cdh_plus_um_memsql_release')

print('\033[31;4m{}\033[0m'.format(123))
