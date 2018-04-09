#*_*coding:utf-8*_*

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
#输入selenium 搜索
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

#移动到 设置
element = driver.find_element_by_name('tj_settingicon')
ActionChains(driver).move_to_element(element).perform()

#单击，弹出的Ajax
driver.find_element_by_link_text('搜索设置').click()

m = driver.find_element_by_xpath('//select[@name="NR"]')
m.find_element_by_xpath('//option[@value="20"]').click()
time.sleep(2)

driver.find_element_by_link_text("保存设置").click()
time.sleep(2)
driver.switch_to_alert().accept()

time.sleep(2)
#driver.quit()