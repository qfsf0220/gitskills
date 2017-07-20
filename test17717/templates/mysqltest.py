import pymysql

db=pymysql.connect('192.168.137.134','root','1234','qfsf')
cursor=db.cursor()
sql='create table usertest (id int,age int,name varchar(10))'
cursor.execute(sql)
db.close()

