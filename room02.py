# coding:utf-8

from selenium  import WebDriver 
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
driver =WebDriver.Chrome()


driver.get("http://mail.163.com/")
time.sleep(3)
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').send_keys('tx')
driver.find_element_by_name('password').send_keys('eq')
driver.quit()










