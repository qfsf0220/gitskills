from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
import pymysql

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@192.168.137.134/qfsf'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref='role')


    def __repr__(self):
        return '<Role %r>' % self.name
class User(db.Model):
    __tablename__='users'
    id =db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>'% self.username
#
# db.create_all()
# admin_role=Role(name='admin')
# mod_role=Role(name='Moder')
# user_role=Role(name='User')
# user_a=User(username='a',role=admin_role)
# user_b=User(username='b',role=mod_role)
# user_c=User(username='c',role=user_role)
#
# db.session.add(admin_role)
# db.session.add(user_role)
# db.session.add(user_a)
# db.session.add(user_c)
#
# db.session.commit()

class abc(db.Model):
    __tablename__='abc'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True)
    email=db.Column(db.String(30),unique=True)

    def __init__(self,username,email):
        self.username=username
        self.email=email

    def __repr__(self):
        return '<abc %r>' % self.username

db.create_all()

for i in ['qf','sf','qpr','we','are','family']:
    # db.session.add('abc("%s","%s@%s.com")'%(i,i,i) )
    "abc('%r','%r@%r.com')"%(i,i,i)
db.session.commit()
print("insert ok.")
# user1=abc('qf','qf@qf.com')
# user2=abc('sf','sf@sf.com')
# user3=abc('qpr','qpr@qpr.com')
# user4=abc('we','we@we.com')
# user5=abc('are','are@are.com')
# user6=abc('family','family@family.com')
#
# db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)
# db.session.add(user4)
# db.session.add(user5)
# db.session.add(user6)
# db.session.add(abc('abc','abc@abc.com'))
#
# db.session.commit()
# print("insert ok.")