
from flask import Flask,render_template


from  flask  import  request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<b><span style=color:yellowgreen>H</span>ello <span style=color:yellowgreen>W</span>orld!</b>'
@app.route('/<name>')
def name(name):
    user_agent = request.headers.get('User-Agent')
    return '<b> 弄好啊,%s</b><br><br> 你的浏览器是:%s'% (name,user_agent)

@app.route('/asdasd/<aa>')
def aa(aa):
    return " 你访问的 %s 404  没有这个页面。" % aa

@app.route('/test')
def templates():
    user={"myname":"qf"}
    familys=[
        {'family':{'name':'sf'},
        'age':30},
        {'family':{'name':'qpr'},
         "age":3
         }
    ]
    return render_template('thirdpage.html',title="hello",user=user,familys=familys)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)
