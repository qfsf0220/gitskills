from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def search():
    browser.get("http://www.taobao.com")
    input = wait.until(
        EC.presence_of_all_elements_located(By.CSS_SELECTOR,"#q")
    )
    submit = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable(By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button")
    )
    input.send_keys("ipad")
    submit.click()


def main():
    search()

if __name__ == '__main__':
    main()