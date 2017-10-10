# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://testadmin.fantem-gateway.com/")
driver.implicitly_wait(20)
#driver.find_element_by_link_text('Login').click()
driver.find_element_by_id('username').send_keys('qw')
driver.find_element_by_id('password').send_keys(1)
driver.find_element_by_xpath("html/body/app-layout/div/div/div/div/div/form/div[5]/div/input").click()
driver.find_element_by_xpath("/html/body/app-layout/div/div/div[1]/layout-menu/div/accordion/div/div[2]/div[1]/h4/a/span").click()
driver.find_element_by_link_text("固件列表").click()
driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/div/div/button").click()
s=driver.find_element_by_xpath("//*[@id='_product']")
Select(s).select_by_value('11')
# driver.find_element_by_xpath("//*[@id='_swVersion']").send_keys("V2.0.3.2")
driver.find_element_by_id("Gamma").click()
driver.find_element_by_id("_username").send_keys("test_firmware")
driver.find_element_by_id("_password").send_keys("test_firmware_password")
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
driver.find_element_by_id("_newPackage").send_keys('F:\\fengtan\\OOMI_Cube_APP_V2.0.4.18_20170925.apk')
driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/form/div[18]/div[1]/input").click()
time.sleep(90)
driver.quit()





