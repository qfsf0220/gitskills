#-*- coding: utf-8 -*-
import urllib
import re
import time,os
import sys

import django

reload(sys)
sys.setdefaultencoding('utf-8')


def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getpic(html):
    # imglist=re.findall(' src="(.*?\.jpg)"/>', html)
    imglist = re.findall(r' src="(http://img.boodoll.cn/.*?.jpg)"', html)
    img2= re.findall(r'<img id="bigImg" src="(.*?.jpg)',html)
    title=re.findall(r'alt="(.*?)" jqimg',html)
    if title[0].find('*') != -1:
        title = title[0].replace("*","")
    titlex=title[0].replace(' ','').encode('gbk')

    print title
    print titlex
    print img2[0]
    if os.path.exists('d://pic//%s' % titlex):
        pass
    else:
        os.mkdir("d://pic//%s" % titlex)
    time.sleep(1)

    for i in imglist:
        print i
        if i.find('alt')!=-1:
            print "baohan alt"
            i=i.split('"')[0]
        urllib.urlretrieve(i, "D://pic//%s//%s" % (titlex,i.split('/')[-1]))
        time.sleep(1)
        urllib.urlretrieve(img2[0],"D://pic//%s//%s" % (titlex,img2[0].split('/')[-1]))

url=raw_input("the url link:")
html = getHtml(url)

getpic(html)
