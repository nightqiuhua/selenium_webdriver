from selenium import webdriver 
import time 
import os 
from selenium.webdriver.support.ui import WebDriverWait

dr = webdriver.Firefox()
path = 'file://'+os.path.abspath('level_locate.html')
dr.get(path)

dr.find_element_by_link_text('Link1').click()
WebDriverWait(dr,10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())

menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')

webdriver.ActionChains(dr).move_to_element(menu).perform()

time.sleep(5)
dr.quit()