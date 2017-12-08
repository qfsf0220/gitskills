import requests
from pyquery import PyQuery as pq
import  re
import  pymysql

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"pgv_pvi=7850858496; pgv_si=s466483200; PHPSESSID=tbpj46in5g171k3qt5r1r03q70; kds_sqrcode=1; Hm_lvt_e8499b7329e8d5d44f3f4c8902bb043a=1512361097,1512612006,1512612259,1512613337; Hm_lpvt_e8499b7329e8d5d44f3f4c8902bb043a=1512615286",
"Host":"club.pchome.net",
"Referer":"http://club.pchome.net/f_15_0_0_1_0.html?page=10",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
conn= pymysql.Connect(host='qfsf0220.win',port=3306,user='root',passwd='Alternatively_qzone_json',db='sspanel',charset='utf8')
print("connect mysql ok.")
cursor=conn.cursor()
# cursor.execute("INSERT into kds (fangwenliang,title,huifuliang,author,submission_date,reader,read_date) VALUES('1.2w','这是test2',1232,'qf','17-12-05 17:20','test','12-06 16:31')")
# cursor.execute('insert into kds (fangwenliang,title,author,reader) VALUES ("1.2w","qqq","qf","test")')



def get():
    for i in range(2,100):
        print("#"*20+"http://club.pchome.net/f_15_0_0_%d_0.html" % i)
        a = requests.get(url="http://club.pchome.net/f_15_0_0_%d_0.html" % i,headers=headers)
        an = pq(a.text)
        for i in range(4,100):
            everytitle= (an('li.i2').eq(i).text() )

            try:
                if everytitle!="":
                    zaza = re.search(r'(\( 1.* \))',everytitle).group()
                    b= (everytitle.replace(zaza,''))
                    listb=(re.findall(r'(\S+)',b)  )
                    print(listb)
                    if len(listb) <=9:
                        try:
                            listb = [listb[0], listb[1], listb[2], listb[3], listb[4] + " " + listb[5], listb[6],'17-'+listb[7] + " " +listb[8]]
                        except IndexError as e:
                            pass
                        sql = "INSERT into kds (fangwenliang,title,huifuliang,author,submission_date,reader,read_date) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (listb[0], listb[1], listb[2], listb[3], listb[4], listb[5], listb[6])

                        cursor.execute(sql)
                        conn.commit()

            except AttributeError as e:
                if everytitle!="":
                    # print(re.findall(r'(\S+)',everytitle) )
                    listb=(re.findall(r'(\S+)',everytitle) )
                    print(listb)
                    if len(listb) <=9:
                        try:
                            listb = [listb[0], listb[1], listb[2], listb[3], listb[4] + " " + listb[5], listb[6],'17-'+listb[7] + " " +listb[8]]
                        except IndexError as e:
                            pass

                        sql = "INSERT into kds (fangwenliang,title,huifuliang,author,submission_date,reader,read_date) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (listb[0], listb[1], listb[2], listb[3], listb[4], listb[5], listb[6])
                        cursor.execute(sql)
                        conn.commit()



get()
conn.commit()

cursor.close()
conn.close()

# conn= pymysql.Connect(host='bdm275214593.my3w.com',port=3306,user='bdm275214593',passwd='1234qwer',db='bdm275214593_db',charset='utf8')
#                         cursor=conn.cursor()
#                         sql = "INSERT into kds (fangwenliang,title,huifuliang,author,submission_date,reader,read_date) VALUES(%s,%s,%s,%s,%s,%s,%s)" % (listb[0], listb[1], listb[2], listb[3], listb[4], listb[5], listb[6])
#                         cursor.execute(sql)
#                         print(cursor.rowcount)
#                         cursor.close()
#                         conn.close()