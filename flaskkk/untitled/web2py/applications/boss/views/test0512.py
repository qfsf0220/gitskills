#__auther__='feng.qian'
# -*- coding: utf-8 -*-
import urllib


def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

html = getHtml("http://item.muyingzhijia.com/153198.html")

print html