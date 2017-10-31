import logging
# logging.basicConfig(level=logging.DEBUG,filename="./123.txt",filemode="a",format='%(asctime)s - %(levelname)s - [line:%(lineno)d]: %(message)s')
#创建一个logger
class logtest():
    def test001(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)#总等级

        logfile ="./logger.txt"
        filehandler = logging.FileHandler(logfile,mode='a')
        filehandler.setLevel(logging.DEBUG)#输出到file的log等级 ，debug 及 更高级别会写文件。

        screenhandler   = logging.StreamHandler()
        screenhandler.setLevel(logging.WARNING)#输出到控制台的log等级，warning 及更高级别会写文件

        outformat= logging.Formatter('%(asctime)s - %(levelname)s - [line:%(lineno)d]: %(message)s')
        """logging.basicConfig函数中，可以指定日志的输出格式format，这个参数可以输出很多有用的信息，如上例所示：
        %(levelno)s: 打印日志级别的数值
        %(levelname)s: 打印日志级别名称
        %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s: 打印当前执行程序名
        %(funcName)s: 打印日志的当前函数
        %(lineno)d: 打印日志的当前行号
        %(asctime)s: 打印日志的时间
        %(thread)d: 打印线程ID
        %(threadName)s: 打印线程名称
        %(process)d: 打印进程ID
        %(message)s: 打印日志信息
        我在工作中给的常用格式在前面已经看到了。就是：
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        这个格式可以输出日志的打印时间，是哪个模块输出的，输出的日志级别是什么，以及输入的日志内容。
        """
        filehandler.setFormatter(outformat)
        screenhandler.setFormatter(outformat)
        logger.addHandler(filehandler)
        logger.addHandler(screenhandler)

        logger.info("info")
        logger.debug("debug")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")


    def main(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("111 test start!")
        logging.info("111------------")
        self.test001()
        logging.info("222------------")
        logging.info("222 test stop!")

if __name__ == '__main__':
    logtest = logtest()
    logtest.main()


