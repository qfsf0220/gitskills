import logging
logging.basicConfig(level=logging.DEBUG,filename="./123.txt",filemode="a",format='%(asctime)s - %(levelname)s - [line:%(lineno)d]: %(message)s')

logging.info("info")
logging.debug("debug")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
print("done")
