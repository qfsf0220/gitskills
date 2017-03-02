# -*- coding: utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse

def index(aaa):
    return HttpResponse(u'弄好boss')


def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(u'获取 2个数据a:%s,b:%s 答案是%s' %(a,b,c))

def welcome(af):
    return  HttpResponse('这个是一个简单的欢迎界面  试一试。。，。。。')


def add2(rr,a=0,b=0):
    c=int(a)+int(b)
    return HttpResponse(str(c))


from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def old_add2_redirect(asd,a,b):
    return HttpResponseRedirect(reverse('add2',args=(a,b)))


def test1(reques):
    return render(reques,'test1.html')
