import builtwith

# builtwith.parse("https://try.taobao.com")
print(  builtwith.parse("http://www.taobao.com") )



import whois as wi


# print( whois.do_parse("http://www.taobao.com"))


w=wi.whois("www.taobao.com")
print(w)

import urllib.robotparser as ur
from urllib.robotparser import RobotFileParser as urf2

# urf = ur.RobotFileParser()
# urf2.set_url("http://qq.win/robot.txt")
# urf2.read()



