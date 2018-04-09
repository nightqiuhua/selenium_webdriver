from selenium import webdriver 
import time 

browser = webdriver.firefox()
browser.get('http://mail.whut.edu.cn')

browser.add_cookie({'name':'key-aaaaaaa','value':'value-bbbb'})

for cookie in browser.get_cookies():
	print('%s -> %s' % (cookie['name'],cookie['value']))

browser.delete_cookie('CookieName')

browser.delete_all_cookies()

time.sleep(2)
browser.quit()