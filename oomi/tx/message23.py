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
driver.find_element_by_xpath(".//*[@id='_title']").send_keys('刚进入NBA的时候,很多人认为他只是一个角色球员.')
driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('刚进入NBA的时候,很多人认为他只是一个角色球员,很难生存下去.后来,人们觉得他有可能成为球队首发.又过了一段时间,他成为了全明星.到最后,他成为了篮球史上的超级巨星.　2017年,人们称李卫为篮球皇帝,王朝教父,史上最伟大的球员和教练,超越神的男人,穿着球衣的上帝,是他,让邓肯')
driver.find_element_by_xpath(".//*[@id='_Touch']").click()
driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input").click()
driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
driver.find_element_by_xpath("//*[@id='_MessageTypeC']").click()
js = ('window.scrollTo(0,document.body.scrollHeight)')
driver.execute_script(js)
time.sleep(3)

driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()

driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
driver.quit()
