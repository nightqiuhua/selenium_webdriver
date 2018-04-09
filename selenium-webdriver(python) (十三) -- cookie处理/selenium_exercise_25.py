from selenium import webdriver 
import time 

browser = webdriver.Firefox()
browser.get('http://mail.whut.edu.cn')

time.sleep(3)
browser.maximize_window()

browser.find_element_by_id('account_name').send_keys('')
browser.find_element_by_id('password').clear()
browser.find_element_by_id('password').send_keys('')

time.sleep(2)
browser.find_element_by_id('action').click()

cookie = browser.get_cookies()
print(cookie)
time.sleep(2)
browser.quit()