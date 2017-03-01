from flask import Flask
from flask import  render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('yemian.html')

@app.route('/<name>')
def hello_name(name):
    return 'hello <h1>%s<h1>' % name






if __name__ == '__main__':
    app.run()
