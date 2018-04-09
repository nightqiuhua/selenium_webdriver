from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time 
import os 

browser = webdriver.Firefox() 
browser.get('http://www.baidu.com')

link= browser.find_element_by_link_text('设置')
ActionChains(browser).move_to_element(link).perform()

time.sleep(2)
browser.find_element_by_link_text('搜索设置').click()

m = browser.find_element_by_name('NR')
m.find_element_by_xpath('//option[@value="50"]').click()
time.sleep(3)

browser.find_element_by_link_text('保存设置').click()
time.sleep(3)
browser.switch_to_alert().accept()

browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
time.sleep(3)
browser.quit()