#-*- coding:utf-8 -*-
from flask import redirect, request, render_template, Flask,abort,flash,url_for
from wtforms import Form #表单类

from wtforms.fields import TextField,StringField,PasswordField
from wtforms import validators
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from db import *
from wtforms import Form, BooleanField, TextField, PasswordField, validators


app = Flask(__name__)



class LoginForm(Form):
    # username=TextField("username",[validators.Required()])
    # password=PasswordField("password",[validators.Required()])
    username=StringField(validators=[DataRequired(),Length(2,20)])
    password=PasswordField(validators=[DataRequired()])

@app.route('/register',methods=['GET','POST'])
def register():
    form =LoginForm(formdata=request.form)
    if request.method=="POST" and form.validate():
        username=form.username.data
        password=form.password.data
        if isExisted(username,password):
            return "已经注册了<a href='http://127.0.0.1:8080/main'>进入主页</a>"
        else:
            addUser(username,password)
            return "<div align='center'><h2 style='color:red'>register success.</h2></div> \
        <a href='http://127.0.0.1:8080/main'>返回主页</a>"
    return  render_template('index.html',form=form)

@app.route('/user',methods=['GET','POST'])
def login():
    form = LoginForm(formdata=request.form)
    if request.method== "POST" and form.validate():
        # return 'error'
        username=form.username.data
        password=form.password.data

        if username=='admin' and password=='12qqssff34':
            return redirect("http://www.163.com")
        elif isExisted(username,password):
            return redirect("http://www.163.com")
        else:
            message="login failed"
            return render_template('index.html', message=message,form=form)
    # return render_template('index.html')
    return render_template('index.html', form=form)

@app.route('/')
def index():
    return '<div align="center"><hqf2>Hello boss</h2> \
           <a href="http://127.0.0.1:8080/register">请先注册</a> \
           </div>'

@app.route('/main')
def main():
    return "welcome boss"

if __name__ == '__main__':
    app.run(port=8080)
