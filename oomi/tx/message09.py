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

driver.find_element_by_id('username').send_keys('qw')
driver.find_element_by_id('password').send_keys(1)
driver.find_element_by_xpath("html/body/app-layout/div/div/div/div/div/form/div[5]/div/input").click()
driver.find_element_by_xpath("//div[@class='panel-group']//span[.='消息推送']").click()
time.sleep(5)

driver.find_element_by_xpath('html/body/app-layout/div/div/div[1]/layout-menu/div/accordion/div/div[5]/div[2]/div/ul/li[1]/a').click()
driver.find_element_by_xpath(".//*[@id='_title']").send_keys('Timing')
driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('Timing')
driver.find_element_by_xpath(".//*[@id='_Touch']").click()
driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input").click()
driver.find_element_by_xpath("//*[@id='_pushTime']").click()
js = 'document.getElementById("dtp_input1").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id("dtp_input1").clear()
driver.find_element_by_id("dtp_input1").send_keys("2017-09-28 16:00:00")
time.sleep(3)
driver.find_element_by_id("_title").click()
driver.find_element_by_xpath("//*[@id='_MessageTypeC']").click()
js = ('window.scrollTo(0,document.body.scrollHeight)')
driver.execute_script(js)
time.sleep(3)
driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()

driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
driver.quit()