from selenium import  webdriver

#
# b = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#
# b.get("http://www.baidu.com")

def openWeb():
    b = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    b.get("http://172.16.96.100:8080/am/page/portal/realm/2e0d1ff9-c070-4e05-a07e-23325461e9db/login/pc/index.html?stage=2&revisit=false&language=zh-CN&portalSessionId=ZM7IU68NTP&tenantId=c3fe9a4b-3475-41c5-9ebc-dbcc9222bf8b&tenantName=Sumscope&amExtraParams=%7B%7D&tenantType=%E5%85%B6%E4%BB%96")

    print(b.title)
    # assert "百fsdf度" in b.title

if __name__=='__main__':
    openWeb()
    input("do not close")