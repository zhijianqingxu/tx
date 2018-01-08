# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(20)
#driver.find_element_by_link_text('Login').click()
driver.find_element_by_id('kw').send_keys('qw')
driver.find_element_by_id('su').click()

time.sleep(5)
driver.quit()





