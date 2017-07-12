import paramiko
import sys,os
import configparser
from functools import reduce

conf= configparser.ConfigParser()
conf.read('config.ini')
conf1=conf.get('conf1','conf')
conf2=conf.get('conf2','conf')

class Comm:
    def __init__(self,ip,port,user,password,mysql_password):
        self.ip= ip
        self.port=port
        self.user=user
        self.password= password
        self.mysql_password=mysql_password

    def run_cmd(self,cmd):
        try:
            trans=paramiko.Transport((self.ip,self.port))
            trans.connect(username=self.user,password=self.password)
            ssh =paramiko.SSHClient()
            ssh._transport=trans
            a,b,c=ssh.exec_command(cmd)
            if b.channel.recv_exit_status()==0:
                stdout=b.readlines()
                # for i in stdout:
                #     print(i)
                return stdout
            else:
                stderr=c.readlines()
                # for i in stderr:
                #     print(i)
                return stderr
        except Exception as e :
            print(e)
        finally:
            trans.close()

    def  sftpfile(self,localpath,remotepath,*args):
        try:
            trans=paramiko.Transport((self.ip,self.port))
            trans.connect(username=self.user,password=self.password)
            sftp =paramiko.SFTPClient.from_transport(trans)
            files=[x for x in args]
            print(reduce(lambda x,y: x+','+y,files)+' where be thansfor')
            for f in files:
                sftp.put(os.path.join(localpath,f),remotepath+'/'+f,callback=self.progress_bar)
        except Exception as e:
            print(e)

    def progress_bar(self,transferred, toBeTransferred, suffix=''):
        bar_len = 60
        filled_len = int(round(bar_len * transferred / float(toBeTransferred)))
        percents = round(100.0 * transferred / float(toBeTransferred), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
        sys.stdout.flush()

class config(Comm):
    def install_mysql(self,my_cnf):
        super().run_cmd("echo 'export PATH=$PATH:/sumscope/mysql/bin' >> /etc/profile && source /etc/profile")
        super().run_cmd(
            'yum install -y libaio && mkdir /sumscope && tar xf  mysql5.6.22.tar -C /sumscope && mv /sumscope/my.cnf /etc/my.cnf && mv /sumscope/mysqld /etc/init.d/mysqld &&chown -R mysql. /sumscope/mysql ')
        super().run_cmd("echo '%s'"%(my_cnf))
        super().run_cmd('mysql -uroot -p{0} -S /opt/sumscope/mysql/mysql.sock -e "grant replication slave, replication client on *.* to \'repl\'@\'{1}\' identified by \'1234\';"  ' .format(self.mysql_password,self.ip))
        super().run_cmd('mysql -uroot -p%s -S /opt/sumscope/mysql/mysql.sock -e " flush privileges;" '%(self.mysql_password))

    def get_pos(self):
        a=super().run_cmd('mysql -uroot -p%s -S /opt/sumscope/mysql/mysql.sock  -e " show master status;  "'%(self.mysql_password))
        file = a[1].split('\t')[0]
        pos = a[1].split('\t')[1]
        return (file,pos)



comm=config(conf.get('host1', 'ip'),int(conf.get('host1', 'port')),conf.get('host1', 'user'),conf.get('host1', 'password'),conf.get('mysql','root_password'))

# comm.run_cmd('ls /tmp')
comm.install_mysql(conf1)
pos1,pos2=comm.get_pos()
print(pos1)
print(pos2)




# comm.sftpfile('E:\\htmltest\\this-a-test','/tmp','README.md','webstormfirst.html')
# comm.run_cmd('yum install -y libaio && mkdir /sumscope && tar xf  mysql5.6.22.tar -C /sumscope && mv /sumscope/my.cnf /etc/my.cnf && mv /sumscope/mysqld /etc/init.d/mysqld &&chown -R mysql. /sumscope/mysql ')

