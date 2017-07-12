import paramiko
import sys
import uuid
import configparser
conf= configparser.ConfigParser()
conf.read('config.ini')
"""
[host1]
ip=172.17.0.2
port=22
user=root
password=1234qwer
[host2]
ip=172.17.0.3
port=22
user=root
password=1234qwer
"""
class Comm:
    def __init__(self,ip,port,user,password):
        self.ip=ip
        self.port=port
        self.user=user
        self.password= password
    def