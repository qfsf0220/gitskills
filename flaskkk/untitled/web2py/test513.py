#__auther__='feng.qian'
# -*- coding: utf-8 -*-

import urllib
import re


def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html



def getpic(html):
    reg=re.findall(r'src=\"(.*),jpg',html)
    return reg

html = getHtml("http://item.muyingzhijia.com/153198.html")

print getpic(html)