from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from pyquery import PyQuery as pq
import re

# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
phantomjs_args=['--load-images=false','--disk-cache=true'] #不加载图片， 开启磁盘缓存
browser = webdriver.PhantomJS(executable_path="C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe",  service_args=phantomjs_args)
browser.set_window_size(1400,900)#默认大小可能会影响 selenium操作
wait = WebDriverWait(browser,11)
def search():
    print("start search")
    try:
        browser.get("https://www.taobao.com")
        myinput = wait.until(
            EC.presence_of_element_located ((By.CSS_SELECTOR,"#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button"))
        )
        myinput.send_keys('美食')
        submit.click()

        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        parse_page()
        return (total.text)
    except TimeoutException:
        return search() #如果请求超时，这里是重试 search()

def next_page(page_number):
    print("现在是"+str(page_number)+"页:")
    try:
        myinput = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        myinput.clear()
        myinput.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page_number)))
        parse_page()
    except TimeoutException:
        next_page(page_number)

def parse_page():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
    html=browser.page_source
    d = pq(html)
    items = d("#mainsrp-itemlist .items .item").items()
    for i in items:
        product ={
            # "image": i.find('.pic .img').attr("src"),
            "price":i.find('.price').text()[1:],
            "buynum":i.find(".deal-cnt").text()[:-3],
            "title":i.find('.title').text(),
            "shopname":i.find(".shop").text(),
            "location":i.find(".location").text(),
            "baoyou": "1" if i.find(".ship") else "0",
            "tmall":"1" if i.find(".icon-service-tianmao") else "0",
            "yunfeixian":"1" if i.find(".icon-service-baoxian") else "0",
            "jinpaimaijia":"1" if i.find(".icon-service-jinpaimaijia") else "0"

        }
        print(product)

def main():
    total= search()
    total = int(re.search(r'(\d+)',total).group(1))
    # for i in range(2,total+1):
    for i in range(2,10):
        next_page(i)

if __name__ == '__main__':
    main()
    parse_page()