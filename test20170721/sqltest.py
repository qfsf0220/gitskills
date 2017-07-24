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

lx=['qf','zk','ypq','xxd','yy','yunwei']
lx2 =list( map(lambda x: ('abc("%s","%s@%s.com")'% (x,x,x)),lx) )
userlist=['user'+str(x+1) for x in range(len(lx))]


xx=list(zip(userlist,lx2))
xx2= list(map(lambda x:x[0]+'='+x[1],xx))

for i in xx2:
    exec(i)

# for i in userlist:
#     exec('db.session.add(%s)' % i)
#
# db.session.commit()
# print("insert ok.")

#####select
uuu = abc.query.all()
# print(uuu)
findout=abc.query.filter_by(id=3).first()
# findout=abc.query.filter(abc.id=='3').first()
print(findout)
# print(qf.username)
# print(qf.email)
findout_3_1=abc.query.limit(1).offset(3)#从第三行开始选 选1行
print(findout_3_1)
#####update
yunwei=abc.query.filter_by(username='yunwei').first()
yunwei.email='aaaaaa@aaaaa.com'
db.session.add(yunwei)
db.session.commit()


###delete
yy= abc.query.filter_by(username='yy').first()
db.session.delete(yy)
db.session.commit()





