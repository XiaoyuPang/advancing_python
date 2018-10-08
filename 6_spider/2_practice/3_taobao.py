'''selenium 模拟浏览器抓取淘宝商品类信息'''

from selenium import webdriver                  #浏览器驱动对象
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
    
browser = webdriver.Chrome()                    #声明驱动对象
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id('kw')    #百度的input输入框
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)                 #模拟回车键
    wait = WebDriverWait(browser,10)            #调用等待

    #等待某个元素WebDriverWait加载，这里是等待content_left
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.get_cookie)
    print(browser.current_url)
    print(browser.page_source)
    
finally:
    browser.close()


