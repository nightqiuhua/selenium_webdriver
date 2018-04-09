from selenium import webdriver 
import time 

browser = webdriver.Firefox()
first_url = 'http://www.baidu.com'

print('now access on %s' %(first_url))
browser.get(first_url)
time.sleep(2)

second_url ='http://news.baidu.com'
print('now access on %s'%(second_url))
browser.get(second_url)
time.sleep(2)

print('back to %s' %(first_url))
browser.back()
time.sleep(2)

print('forward to %s' %(second_url))
browser.forward()
time.sleep(2)

browser.quit()