import paramiko
import sys,os
import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read('config.ini')
conf1=conf.get('conf1','conf')
conf2=conf.get('conf2','conf')
ip1=conf.get('host1','ip')
ip2=conf.get('host2','ip')

class Comm(object):
    def __init__(self,ip,port,user,password,mysql_password):
        self.ip=ip
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
            print(cmd)
            a,b,c=ssh.exec_command(cmd)
            if b.channel.recv_exit_status()==0:
                stdout=b.readlines()
                for i in stdout:
                    print(i)
                return stdout
            else:
                stderr=c.readlines()
                for i in stderr:
                    print(i)
                return stderr
        except Exception , e :
            print(e)
        finally:
            trans.close()

    def sftpfile(self, localpath, remotepath, *args):
        try:
            trans = paramiko.Transport((self.ip, self.port))
            trans.connect(username=self.user, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(trans)
            files = [x for x in args]
            print(reduce(lambda x, y: x + ',' + y, files) + ' where be thansfor')
            for f in files:
                sftp.put(os.path.join(localpath, f), remotepath + '/' + f, callback=self.progress_bar)
        except Exception, e:
            print(e)

    def progress_bar(self, transferred, toBeTransferred, suffix=''):
        bar_len = 60
        filled_len = int(round(bar_len * transferred / float(toBeTransferred)))
        percents = round(100.0 * transferred / float(toBeTransferred), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
        sys.stdout.flush()


class config(Comm):
    def install_mysql(self, my_cnf, ip):
        super(config, self).run_cmd("echo 'export PATH=$PATH:/sumscope/mysql/bin' >> /etc/profile && source /etc/profile")
        super(config, self).run_cmd('yum install -y libaio && mkdir -p /sumscope && tar xf  /tmp/mysql5.6.22.tar -C /sumscope &&mkdir -p /sumscope/mysql/{run,log} && mv /sumscope/mysql/data/auto.cnf  /sumscope/mysql/data/auto.cnf.bak    && mv /sumscope/mysqld /etc/init.d/mysqld &&  chown -R mysql. /sumscope/mysql ')
        super(config, self).run_cmd("echo '%s' > /etc/my.cnf" % (my_cnf))
        super(config, self).run_cmd("/etc/init.d/mysqld start")
        super(config, self).run_cmd('mysql -uroot -h127.0.0.1 -e "grant replication slave, replication client on *.* to \'repl\'@\'{0}\' identified by \'1234\';"  '.format(ip))
        super(config, self).run_cmd('mysql -uroot -h127.0.0.1 -e " flush privileges;" ')
        # @staticmethod
        def get_pos(self):
            a = super(config, self).run_cmd('mysql -uroot -h127.0.0.1 -e " show master status;  "')
            file = a[1].split('\t')[0]
            pos = a[1].split('\t')[1]
            return (file, pos)

        def start_slave(self, ip):
            super(config, self).run_cmd("mysql -uroot -h127.0.0.1 -e \"change master to master_host='{0}',master_user='repl', master_password='1234', master_port=3306, master_log_file='{1}', master_log_pos={2}, master_connect_retry=30; \"".format(ip, self.get_pos()[0], self.get_pos()[1]))
            super(config, self).run_cmd("mysql -uroot -h127.0.0.1 -e 'start slave;'")

if __name__ == '__main__':
    print("start host1")
    comm = config(conf.get('host1', 'ip'), int(conf.get('host1', 'port')), conf.get('host1', 'user'),conf.get('host1', 'password'), conf.get('mysql', 'root_password'))
    comm.sftpfile('.', '/tmp', 'mysql5.6.22.tar')
    comm.install_mysql(conf2, ip2)
    file, pos = comm.get_pos()
    print(file + ' ' + pos)
    print("start host2")
    comm2 = config(conf.get('host2', 'ip'), int(conf.get('host2', 'port')), conf.get('host2', 'user'),conf.get('host2', 'password'), conf.get('mysql', 'root_password'))
    comm2.sftpfile('.', '/tmp', 'mysql5.6.22.tar')
    comm2.install_mysql(conf1, ip1)
    file, pos = comm2.get_pos()
    print(file + ' ' + pos)
    print("start slave")
    comm.start_slave(ip2)
    comm2.start_slave(ip1)