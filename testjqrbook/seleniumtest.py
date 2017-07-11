from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from  pyquery import PyQuery as pq
import requests
import time,re


bb = webdriver.Chrome(executable_path='C:\\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe')

bb.implicitly_wait(20)


url = 'http://www.qianfanedu.cn/forum-47-1.html'
bb.get(url)
# link = bb.find_element_by_link_text("交流")
# link2 = bb.find_element_by_link_text("学前教育")
# link.click()
# link2.click()

bu= bb.find_element_by_id('ls_username')
bu.send_keys('qfsf0220')
bp= bb.find_element_by_id('ls_password')
bp.send_keys('1234qwer')
bp.submit()


a =requests.get(url)
text = a.text
data = pq(text)
# titlelist = re.findall(r'normalthread_\d{5}',text)
titlelist = re.findall(r'class="s xst">(.*)</a>',text)

# titlelist = data('[onclick="atarget(this)"]').text().split(' ')
# print(titlelist)
titlelist = titlelist[0:5]
print(titlelist)

])
    a+=1
    # time.sleep(5)
    # btext = bb.find_element_by_id('fastpostmessage')
    # btext.send_keys("新手过来膜拜一下各位大神，向各位学习。。")






