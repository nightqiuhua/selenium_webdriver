from selenium import webdriver
import time 

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
time.sleep(2)

data = browser.find_element_by_id('cp').text
print('data=',data)
time.sleep(2)

browser.quit()

