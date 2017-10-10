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
driver.find_element_by_xpath(".//*[@id='_title']").send_keys('Hello, oomi. Welcome to this big family！alphar ')
driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('Hello, oomi. Welcome to this big family！alphar ')
driver.find_element_by_xpath("//*[@id='_Android']").click()

driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/form/div[7]/div/label[3]/input").click()
driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
js = ('window.scrollTo(0,document.body.scrollHeight)')
driver.execute_script(js)
time.sleep(3)

driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()

driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
driver.quit()