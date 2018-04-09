from selenium import webdriver 
import time 

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
time.sleep(2)

browser.find_element_by_id('kw').clear()
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()

time.sleep(3)
browser.quit()