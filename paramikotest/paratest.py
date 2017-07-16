__author__ = 'qfsf'
import paramiko
import configparser

class ParamikoClient:
    def __index__(self):
        self.config=configparser.ConfigParser()
        self.config.read('config.ini')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(hostname=self.config.get('host1','host'),
                           port=int(self.config.get('host1','port')),
                           username=self.config.get('host1','username'),
                           password=self.config.get('host1','password'),
                           timeout=10.0,
                           allow_agent=False,
                           look_for_keys=False)
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass
    def run_cmd(self,cmd):
        stdin,stdout,stderr=self.client.exec_command(cmd)
        for i in stdout:
            print(i)


client=ParamikoClient()
client.connect()
client.run_cmd('date')