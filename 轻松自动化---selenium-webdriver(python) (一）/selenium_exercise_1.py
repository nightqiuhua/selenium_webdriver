from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
print(browser.title)#打印网页头
time.sleep(1)#休眠
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
time.sleep(5)
browser.quit()