from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com')
browser.implicitly_wait(10)
# 웹사이트 열기

browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_3CUDs')
search.click()
#검색창 클릭

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

before_h = browser.execute_script("return window.scrollY")

while True:
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
    
    time.sleep(2)
    
    after_h = browser.execute_script("return window.scrollY")
    
    if after_h == before_h:
        break
    before_h = after_h
#스크롤 내리기

items = browser.find_elements(By.CSS_SELECTOR, 'basicList_info_area__TWvzp')

for item in items:
    name = item.find_element(By.CSS_SELECTOR, 'basicList_title__VfX3c').text
    price = item.find_element(By.CSS_SELECTOR, 'price_num__S2p_v').text
    link = item.find_element(By.CSS_SELECTOR, 'basicList_title__VfX3c > a').get_attribute('href')
    print(name, price, link)