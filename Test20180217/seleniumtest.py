from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from pyquery import PyQuery as pq
import re
import pymysql

# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
phantomjs_args=['--load-images=false','--disk-cache=true'] #不加载图片， 开启磁盘缓存
browser = webdriver.PhantomJS(executable_path="C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe",  service_args=phantomjs_args)
browser.set_window_size(1400,900)#默认大小可能会影响 selenium操作
wait = WebDriverWait(browser,11)
def search(youwant):
    print("start search")
    try:
        browser.get("https://www.taobao.com")
        myinput = wait.until(
            EC.presence_of_element_located ((By.CSS_SELECTOR,"#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button"))
        )
        myinput.send_keys(youwant)
        submit.click()

        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        parse_page(youwant)
        return (total.text)
    except TimeoutException:
        return search(youwant) #如果请求超时，这里是重试 search()

def next_page(page_number,youwant):
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
        parse_page(youwant)
    except TimeoutException:
        next_page(page_number,youwant)

def parse_page(youwant):
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
    html=browser.page_source
    d = pq(html)
    items = d(".m-itemlist .items .item").items()###

    db = pymysql.connect("localhot", 'root', "1234", "bdm275214593_db")

    db.set_charset("utf8")
    cursor = db.cursor()
    create_table(youwant, cursor, db)

    for i in items:
        productinfo ={
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
        print(productinfo)

        save_data(youwant,cursor,db,productinfo)
    db.close()

def create_table(youwant,cursor,db):
    # db.execute('SET NAMES utf8;')
    # db.execute('SET CHARACTER SET utf8;')
    # db.execute('SET character_set_connection=utf8;')
    createtablesql = "create table if not exists %s (id int not null auto_increment,name nvarchar(50), shopname nvarchar(20),price nvarchar(10),buynum varchar(10),location nvarchar(20),baoyou nvarchar(2),tmall nvarchar(2),yunfeixian nvarchar(2), jinpai nvarchar(2),createtime datetime , PRIMARY key(id)  ) DEFAULT charset=utf8 COLLATE utf8_general_ci" % re.sub('\s','',youwant)
    cursor.execute(createtablesql)
    db.commit()
    # save_data(youwant, cursor, db, product)
    # db.close()

def save_data(youwant,cursor,db,product):
    sql = "insert into %s (name,shopname,price,buynum,location,baoyou,tmall,yunfeixian,jinpai,createtime) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s',now())" % (re.sub('\s','',youwant),product["title"],product["shopname"],product["price"],product["buynum"],product["location"],product["baoyou"],product["tmall"],product["yunfeixian"],product["jinpaimaijia"])
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("insert ok.")
    except Exception as  e:
        print("ERROR"+str(e))
        db.rollback()


def main():
    total= search("三星 s8")
    total = int(re.search(r'(\d+)',total).group(1))
    for i in range(2,total+1):
    # for i in range(2,4):
        next_page(i,"三星 s8")

if __name__ == '__main__':
    main()
