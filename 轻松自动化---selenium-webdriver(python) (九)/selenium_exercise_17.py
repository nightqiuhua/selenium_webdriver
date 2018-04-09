from selenium import webdriver 
import time 
import os 

browser = webdriver.Firefox() 
path = 'file://'+os.path.abspath('upload_file.html')
browser.get(path) 

browser.find_element_by_name('file').send_keys('C:\\Users\\Administrator\\Desktop\\系辞传.doc')
time.sleep(4)

browser.quit()