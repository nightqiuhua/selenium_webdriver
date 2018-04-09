from selenium import webdriver 
import time 
import os 

browser = webdriver.Firefox() 
path = 'file://'+os.path.abspath('js.html')
browser.get(path) 

#browser.execute_script('$("#tooltip").fadeOut();')
#time.sleep(5)

button = browser.find_element_by_class_name('btn')
browser.execute_script('$(arguments[0]).fadeOut()',button)
time.sleep(5)

browser.quit()