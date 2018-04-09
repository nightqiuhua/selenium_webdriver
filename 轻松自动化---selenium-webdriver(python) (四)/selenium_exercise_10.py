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

print(type(checkboxs))
time.sleep(2)

browser.find_elements_by_css_selector("input[type='checkbox']").pop().click()
time.sleep(2)

browser.quit()