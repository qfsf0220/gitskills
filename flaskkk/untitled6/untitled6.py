from flask import Flask,request,render_template,redirect
from wtforms import Form
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length
from flask_bootstrap import Bootstrap

import pymongo

app = Flask(__name__)

Bootstrap(app)


client = pymongo.MongoClient(host='192.168.8.172', port=27017)
db = client.qfsf
t1 = db.t1

def adduser(text1,text2):
    result=db.t1.insert_one({"username":text1,"password":text2})
    return  result

def isexist(text1,text2):
    result=db.t1.find({'username':text1})
    if [x for x in result]:
        return  True
    else:
        return False

class textform(Form):
    text1=StringField('text1',validators=[DataRequired(),Length(2,20)])
    text2=PasswordField('text2',validators=[DataRequired()])

@app.route('/',methods=["GET","POST"])
def hello_world():
    form=textform(formdata=request.form)
    print(form.text1)
    print(form.data['text1'])
    if request.method=="POST" and form.validate():  #如果只是拿前端数据这个if循环不需要
        text1=form.data['text1']  #这里是实例化前段传的数据
        text2=form.data['text2']
        if text1=='111' and text2=='111':   #进行比较
            return redirect("http://www.163.com")
        elif isexist(text1,text2):
            message='账号已存在'
            return render_template('mongo.html',message=message,form=form)
        else:
            adduser(text1,text2)
            message='注册成功'
            return render_template('mongo.html',message=message,form=form)
    return render_template('mongo.html', form=form)

@app.route('/boot')
def aa():
    name='qfsf'
    return render_template('show.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
