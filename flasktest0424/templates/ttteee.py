import paramiko
import  os

class download_setup_etcd(object):
    def __init__(self, ip):
        self.ip = ip
    def download(self):
        os.chdir(download_dir)
        os.system('wget https://github.com/coreos/etcd/releases/download/v3.1.5/etcd-v3.1.5-linux-amd64.tar.gz')
        os.system('tar xzvf etcd-v3.1.5-linux-amd64.tar.gz')
    def setup(self):
        file_list = []
        file = os.listdir(download_dir+'/'+'etcd-v3.1.5-linux-amd64')
        t = paramiko.Transport((self.ip, 22))
        t.connect(username='root', password='kevin')
        for a in filter(lambda x: re.findall('^etcd.*', x), file):
            file_list.append(a)
        for i in file_list:
            remote_file = bin_dir + '/' + i
            local_file = download_dir+'/etcd-v3.1.5-linux-amd64/'+ i
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put(local_file, remote_file)
        t.close()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip,22,"root", "kevin")
        stdin, stdout, stderr = ssh.exec_command('chmod +x %s *' % bin_dir)
        ssh.close()