from flask import Flask,render_template,request,make_response,redirect,abort
from werkzeug.routing import BaseConverter
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

class zhuanhuanqi(BaseConverter):
    def __init__(self,url_map,*items):
        super(zhuanhuanqi,self).__init__(url_map)
        self.regex=items[0]

app = Flask(__name__)
app.url_map.converters['urlzhengze']=zhuanhuanqi
Bootstrap(app)
nav = Nav()

nav.register_element('top',Navbar('Flask',
                                  View('主页','index'),
                                  View('用户','user'),
                                  View('服务','service')
                                  ))

nav.init_app(app)


@app.route('/')
def index():
    user_agent=request.headers.get('User-Agent')
    return '<h3 style=color:yellowgreen>%s</h3>'% user_agent ,206


@app.route('/service')
def service():
    response= make_response("<h4> service .... </h4>")
    response.set_cookie('answter','42')
    return response
@app.route('/about')
def about():
    return  redirect('http://www.w3school.com.cn/')

@app.route('/user/<int:id>')#这里可以int    float  和path
def uuuser(id):
    if not id:
        abort(404)
    return '<h2>User%d</h2>' % id

@app.route('/user/<urlzhengze("\S{6}"):username>')
def pipei_url(username):
    return '<h3 style=color:red>user : %s </h3>'  % username
@app.route('/template')
def template():
    return  render_template('../static/index.html')

if __name__ == '__main__':
    app.run(port=80,debug=True)
