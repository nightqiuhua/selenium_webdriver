from selenium import webdriver 
import time 
browser = webdriver.Firefox()
browser.get('http://m.mail.10086.cn')
time.sleep(2)

print('设置游览器宽480，高800显示')
browser.set_window_size(480,800)
time.sleep(3)
browser.quit()