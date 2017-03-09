#本地端 py2.7.9 测试ok
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko

I = 54

rankid = raw_input( "enter the  rank id number:")
s2=paramiko.SSHClient()       #绑定实例
s2.load_system_host_keys()    #加载本地的  known_hosts
s2.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #忽略第一次连接验证
prikey='/home/AthenaGit/xuxiaoshen-jh'
key=paramiko.RSAKey.from_private_key_file(prikey)
s2.connect('119.254.210.172',11200,'xuxiaoshen',pkey=key,timeout=5)
stdin4,stdout4,stderr4=s2.exec_command('sudo  python2.6 /root/script/ranktop.py %s' % rankid )
cmd_result4=stdout4.read(),stderr4.read()
for i in cmd_result4:
    print(i)


#远程端
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb as mysql
import xlsxwriter
import sys,time,os

rankid = sys.argv[1]
reload(sys)
sys.setdefaultencoding('utf8')

#rankid = raw_input("which ranking? ")


def makeexcel():
    try:
        rankid = sys.argv[1]
        workbook = xlsxwriter.Workbook('ranktop%s.xlsx' % rankid)
        worksheet = workbook.add_worksheet('sheetabc')
        bold = workbook.add_format({'bold':True})

        cmd = 'SELECT * FROM ranking_top_%s ORDER BY score DESC;' % rankid

        conn=mysql.connect(host="192.168.3.254",user="opd2cdb",passwd="KH23NskLk",db="athena_event_cbt",charset="utf8")

        cur=conn.cursor()

        cur.execute(cmd)

        result = cur.fetchall()
        fields = cur.description

        for field in range(0,len(fields)):
                worksheet.write(0,field,fields[field][0],bold)

        for row in range(1,len(result)+1):
            for col in  range(0,len(fields)):
                worksheet.write(row,col,u'%s' % result[row-1][col])

        cur.close()
        conn.close()
        workbook.close()
    except IndexError:
        print('enter the ranking id number.')



def sendmail():
    os.popen("echo 'this is ranktop%s file'|python /root/script/SendmailViaSMTP.py  --host='smtp.exmail.qq.com'  --from=
'feng.qian@opd2c.com' --to='feng.qian@opd2c.com;shuqiao.li@opd2c.com' --user='feng.qian@opd2c.com' --password='111111' -
-subject='ranktop%s file' --attach='ranktop%s.xlsx'" %(rankid,rankid,rankid))

if __name__ == '__main__':
	makeexcel()
	sendmail()
