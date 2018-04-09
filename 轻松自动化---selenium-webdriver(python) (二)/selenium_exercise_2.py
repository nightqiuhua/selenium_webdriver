from selenium import webdriver 
import time 

browser = webdriver.Firefox()
url = 'http://www.baidu.com'
print('now access %s' %(url))
browser.get(url)
time.sleep(1)
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
print(browser.current_url)#打印当前网页地址
time.sleep(5)
browser.quit()
