from selenium import webdriver 
import time 
import os 

browser = webdriver.Firefox()
path = 'file://'+os.path.abspath('drop_down.html')
browser.get(path) 
time.sleep(3)

m=browser.find_element_by_id('ShippingMethod')
m.find_element_by_xpath('option[@value="9.03"]').click()
#m.find_element_by_css_selector()

time.sleep(3)
browser.quit()