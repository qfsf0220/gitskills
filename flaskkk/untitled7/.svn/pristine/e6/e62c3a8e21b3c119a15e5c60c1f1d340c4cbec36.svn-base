#-*- coding:utf-8 -*-
from flask import Flask, render_template, session, g, current_app,request,redirect
import time

import pymysql


app = Flask(__name__)

@app.route("/user",methods=['GET','POST'])
def login():
    if request.method=='post':
        username=request.form['username']
        password=request.form['password']
        if username=='qfsf' and password=='1234':
            return redirect('http://www.baidu.com')
        else:
            message='login error'
            return render_template('test2.html')


@app.route('/')
def index():
  session['user'] = 'qfsf'
  g.db = 'mysql'
  return render_template('test2.html')

@app.context_processor
def appinfo():
  return dict(appname=current_app.name)

@app.context_processor
def get_current_time():
  def get_time(timeFormat="%Y/%m/%d - %H:%M:%S"):
    return time.strftime(timeFormat)
  return dict(current_time=get_time)

@app.context_processor
def get_num():
    def getNum(a,b):
        return a+b
    return dict(xxx=getNum)


@app.route('/sql')
def showsql():
    conn = pymysql.connect(host='192.168.8.186', user='root', passwd='1234', db='test', charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from websites')
    result = cur.fetchall()
    return render_template('test2.html', result=result)


app.secret_key = '123456'


app.run(host='0.0.0.0',port=18080,debug=True)