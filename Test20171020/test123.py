import  time
from selenium import  webdriver
import  unittest
"""http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=6RTWN1AW9Q&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%22terminalAutoLoginTimeout%22%3A%22-247702%22%7D&portalType=87012f5e-1876-4bb9-8b63-5ee8179877f9&tenantType=%E5%85%B6%E4%BB%96&terminalMac=9C%3A5C%3A8E%3A70%3A07%3A4D&loginName=feng.qian&roles=_OPS_all_Technology_All-SH
    """
# b = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#
# b.get("http://www.baidu.com")
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
        elem = driver.find_element_by_name("wd")
        elem.send_keys("paramiko")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='1']/h3/a").click()
        # driver.find_element_by_name("tj_trmap").click()
        # driver.get("https://www.baidu.com/")
        # elem2 = driver.find_element_by_name("tj_trmap")
        # elem2.click()
        print(driver.find_element_by_xpath("//*[@id='1']/h3/a").text)

    def lettest2(self):
        driver = self.driver;
        driver.get("http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=6RTWN1AW9Q&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%22terminalAutoLoginTimeout%22%3A%22-247702%22%7D&portalType=87012f5e-1876-4bb9-8b63-5ee8179877f9&tenantType=%E5%85%B6%E4%BB%96&terminalMac=9C%3A5C%3A8E%3A70%3A07%3A4D&loginName=feng.qian&roles=_OPS_all_Technology_All-SH")
        ee=driver.find_element_by_xpath("/html/body").text
        if "Success" in ee:
            print(ee)
        else:
            elem = driver.find_element_by_xpath("//*[@id='un-userName']")
            elem.send_keys("f.n")
            elem2 = driver.find_element_by_xpath("//*[@id='un-password']")
            elem2.send_keys("x31234qwer")
            elem3 = driver.find_element_by_xpath("//*[@id='un-login']")
            elem3.click()
        time.sleep(15)
        driver.quit()






        print(driver.page_source)
        assert "No Result Found" not in driver.page_source

        def tearDown(self):
            self.driver.close()

if __name__=='__main__':
    cw =checkWeb()
    cw.openWeb()
    cw.lettest2()