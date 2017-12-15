#-*- coding:utf-8 -*-
import time
import os
import sys
import logging
import json
import subprocess
logging.basicConfig(level=logging.WARN,format='%(asctime)s %(filename)s %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename = os.path.join(os.getcwd(),'processlog.txt'),filemode='a')

owner = subprocess.check_output("ps -ef |grep 'python checkprocess' |grep -Ev 'grep'|wc -l",shell=True)
if int(owner) < 2:
    jsonfile = os.path.join(os.getcwd() , 'checkprocess.json' )
    f = open( jsonfile)
    j = json.load(f)

    def startprocess(processname,lockfile,start_cmd):
        os.system("ps -ef |grep %s -i |grep -Ev 'grep|checkprocessnew' >%s" % (processname,lockfile) )
        logging.debug("lockfile size:"+str(os.path.getsize(lockfile))+" "+processname+" is alive.")
        if not (os.path.getsize(lockfile)):
            logging.warning("Restart : '%s'" % processname)
            os.system("%s" % start_cmd)

    while 1:
        logging.debug("start")
        for i in j.keys():
            processname = str(i)
            start_cmd = str(j[processname])
            lockfile = os.path.join(os.getcwd(),'%s.lock' % processname)

            startprocess(processname,lockfile,start_cmd)
        time.sleep(5)
else:
    print("checkprocess.py is running.")