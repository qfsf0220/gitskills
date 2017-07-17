from flask import Flask,render_template,request
from werkzeug.routing import BaseConverter

class zhuanhuanqi(BaseConverter):
    def __init__(self,url_map,*items):
        super(zhuanhuanqi,self).__init__(url_map)
        self.regex=items[0]

app = Flask(__name__)
app.url_map.converters['urlzhengze']=zhuanhuanqi


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<int:id>')#这里可以int    float  和path
def uuuser(id):
    return '<h2>User%d</h2>' % id

@app.route('/user/<urlzhengze("\S{6}"):username>')
def pipei_url(username):
    return 'user : %s' % username

if __name__ == '__main__':
    app.run(port=80,debug=True)
