from selenium import webdriver 
import time 

browser = webdriver.Firefox()
browser.get('http://mail.whut.edu.cn')

cookie = browser.get_cookies()

print(cookie)