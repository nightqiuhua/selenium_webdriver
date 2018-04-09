from selenium import webdriver 
import time 
import os 

browser = webdriver.Firefox()
path = 'file://'+os.path.abspath('checkbox.html')
browser.get(path) 

inputs = browser.find_elements_by_tag_name('input')

for in_put in inputs:
	if in_put.get_attribute('type') == 'checkbox':
		print('in_put=',in_put)
		in_put.click()

time.sleep(2)

browser.quit()