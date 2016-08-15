#-*- encoding:utf-8 -*-
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> This is index page.</h1>'

if __name__=='__main__':
    app.run(host='0.0.0.0')
