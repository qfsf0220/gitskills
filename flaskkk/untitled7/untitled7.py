from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
