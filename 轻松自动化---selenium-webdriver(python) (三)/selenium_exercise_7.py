from selenium import webdriver 
import time 

browser = webdriver.Firefox() 
browser.get('http://www.baidu.com')
time.sleep(2)

browser.find_element_by_link_text('贴吧').click()

time.sleep(2)
browser.quit()