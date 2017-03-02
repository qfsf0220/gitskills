#exec database operation

import pymysql

conn=pymysql.connect(host='192.168.8.186',\
                     user='root',passwd='1234',db='test',charset='utf8')



def addUser(username,password):
    cur = conn.cursor()
    sql="insert into user(username,password) values ('%s','%s')" % (str(username),str(password))
    cur.execute(sql)
    conn.commit()
    cur.close()


def isExisted(username,password):
    cur=conn.cursor()
    sql="select * from user where username='%s' and password='%s'" % (username,password)
    cur.execute(sql)
    result=cur.fetchall()
    if len(result)==0:
        return False
    else:
        return True
    cur.close()


