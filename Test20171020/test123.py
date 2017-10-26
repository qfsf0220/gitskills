import random
import  time
from selenium import  webdriver
import  unittest
import  sys
import datetime

from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException,ElementNotVisibleException,StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

class checkWeb(unittest.TestCase):
    def openWeb(self):
        self.driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def lettest(self):
        driver = self.driver
        # driver.get("http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=ZM7IU68NTP&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=%E5%85%B6%E4%BB%96")
        driver.get("https://www.baidu.com/")
        # driver.maximize_window()
        # self.assertIn("百度",driver.title,"youmeiy python")
        # assert "百fsdf度" in b.title//如果断言错误 程序退出 直接抛出 assertException
        elem =driver.find_element_by_name("username")
        elem = driver.find_element_by_name("wd")
        elem.send_keys("paramiko")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='1']/h3/a").click()
        print(driver.find_element_by_xpath("//*[@id='1']/h3/a").text)

    def lettest2(self):
        driver = self.driver;
        driver.get("http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=6RTWN1AW9Q&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%22terminalAutoLoginTimeout%22%3A%22-247702%22%7D&portalType=87012f5e-1876-4bb9-8b63-5ee8179877f9&tenantType=%E5%85%B6%E4%BB%96&terminalMac=9C%3A5C%3A8E%3A70%3A07%3A4D&loginName=feng.qian&roles=_OPS_all_Technology_All-SH")

        ee=driver.page_source
        if "Success." in ee:
            print("web .. Success")
            try:
                if driver.find_element_by_id("ms-sureBtn"): #//*[@id="ms-sureBtn"]
                    driver.find_element_by_id("ms-sureBtn").click()
                    time.sleep(2)
                    driver.find_element_by_id("refresh").click()#//*[@id="refresh"]
            except NoSuchElementException as e:
                print("Notice: Now Loginng ok. (No element :refresh or ms-sureBtn)")
        else:
            # elem = driver.find_element_by_xpath("//*[@id='un-userName']")
            try:
                elem =driver.find_element_by_id("un-userName")
                elem.send_keys("fq")
                # elem2 = driver.find_element_by_xpath("//*[@id='un-password']")
                elem2 = driver.find_element_by_id("un-password")
                elem2.send_keys("3x1234qwer")
                elem3 = driver.find_element_by_id("un-login")
                print(elem3.text)
                # elem3 = driver.find_element_by_xpath("//*[@id='un-login']")
                elem3.click()
            except NoSuchElementException  as e:
                print("Error: There have no element.")
            except ElementNotVisibleException as e:
                print("Error: Element can not visible.")
            except NoSuchWindowException as e:
                print("Error: Window has been closed.")
            except StaleElementReferenceException as e:
                print("Error: Input info possible wrong.")
        time.sleep(3)
        driver.quit()

        # print(driver.page_source)
        # assert "No Result Found" not in driver.page_source
        def tearDown(self):
            self.driver.close()


# if __name__=='__main__':
int_a = 1
while 1:
    nowtime = (time.asctime(time.localtime()).split(' ')[3].split(':')[0]+time.asctime(time.localtime()).split(' ')[3].split(':')[1])
    if int(nowtime) < 915 and int(nowtime) > 845:
        print("Notice:now almost 9 clock  (%s)" % nowtime)
        cw = checkWeb()
        cw.openWeb()
        cw.lettest2()
    elif int(nowtime) >1830 :
        print("Notice:now has out of office time  (%s)" % nowtime)
        now = time.ctime()
        tomorrowtmp = now.split()
        tomorrowtmp[3]="08:55:00"
        tomorrowtmp[2]=str(datetime.date.today()+datetime.timedelta(days=1)).split('-')[2]
        from functools import reduce
        tomorrow = reduce(lambda x, y: x + ' ' + y, tomorrowtmp)
        print(tomorrow)
        secondtotomorrow = time.mktime(time.strptime(tomorrow,"%a %b %d %H:%M:%S %Y"))-time.mktime(time.strptime(time.asctime()))
        print("wait for " + str(secondtotomorrow)+ " seconds.")
    else:
        print("Notice:now has pass 9 clock  (%s)" % nowtime)
        # print(str("%d") % int_a * 22)
        cw = checkWeb()
        cw.openWeb()
        cw.lettest2()
        int_a += 1
        randomtime = random.randrange(600, 1700)
        print("   - wait for %s seconds" % randomtime)
        time.sleep(randomtime)