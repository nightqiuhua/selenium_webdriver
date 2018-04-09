from selenium import webdriver 
import time 
import os 

browser = webdriver.Firefox()
path = 'file://'+os.path.abspath('checkbox.html')

browser.get(path) 
time.sleep(2)

checkboxs = browser.find_elements_by_css_selector("input[type='checkbox']")
for checkbox in checkboxs:
	checkbox.click()

time.sleep(4)

print(len(browser.find_elements_by_css_selector("input[type='checkbox']")))
browser.quit()