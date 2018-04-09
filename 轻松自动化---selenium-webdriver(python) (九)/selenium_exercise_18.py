from selenium import webdriver 
import os 
import time 

browser = webdriver.Firefox() 
browser.get('http://m.mail.10086.cn')
browser.implicitly_wait(30) 

browser.find_element_by_id('label_user').clear()
browser.find_element_by_id('label_user').send_keys('')
browser.find_element_by_id('txtPass').send_keys('')
browser.find_element_by_class_name('button sureBtn f1').click()
time.sleep(3)

browser.find_element_by_xpath('/html/body/div[3]/a[9]/span[2]').click()
time.sleep(3)

browser.find_element_by_id('id_file').send_keys('D:\\selenium_use_case\\upload_file.txt')
time.sleep(5)

browser.quit()