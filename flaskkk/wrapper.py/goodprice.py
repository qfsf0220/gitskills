# -*- coding:utf-8 -*-
import requests,re,smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from pyquery import PyQuery as pq

import threading


def get_price(url):
    g=re.findall(r'<em id="item_price">(.*?)</em>',x2)
    for i in g:
        return i

def get_name():
    p=pq(x)
    a=p('.breadCrumbs').text()
    ba=a.split('>')
    try:
        return ba[2]
    except:
        pass

def main():
    global x
    global x2
    global ll
    ll=[]
    for i in range(1000000,1000132):
        url='http://www.mia.com/item-%d.html' % i
        # print url
        html=requests.get(url)
        x=html.text
        x2 = x.encode('gbk','ignore')
        if get_name() and get_price(url):
            # print('name:'+get_name(),'\n', 'price:'+get_price(url),'\n','-'*30)
            ll.append(get_name()+'\n'+get_price(url)+'\n'+'-'*30+'\n')
    fileo=open('D:/tmp.txt','w+')
    for i in ll:
        fileo.write(i.encode('utf-8'))
    fileo.close()








def famail():
    msg = MIMEMultipart()
    msg['From'] = 'qianfeng0220@163.com'
    msg['To'] = ''
    msg['Subject'] = 'shangpin test'
    f=open('d:/tmp.txt')
    i=f.readlines()
    stradd=reduce(lambda x, y: x + y, i)
    message = '%s' % stradd
    msg.attach(MIMEText(message,_charset='utf-8'))
    to='82970496@qq.com,feng.qian@opd2c.com'
    to=to.split(',')
    s = smtplib.SMTP('smtp.163.com',25)
    s.login('qianfeng0220','qfsf0220')
    s.sendmail('qianfeng0220@163.com',to,msg.as_string())
    print("mail has send!")
    f.close()
    s.quit()


if __name__=='__main__':
    t = threading.Thread(target=main())
    t.start()
    t.join()
    famail()