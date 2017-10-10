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
driver.find_element_by_xpath(".//*[@id='_title']").send_keys("I believe Kendall wanted the American Idol audition so much that she willed herself to move again. One of her friends bro")
driver.find_element_by_xpath(".//*[@id='_massage']").send_keys("I believe Kendall wanted the American Idol audition so much that she willed herself to move again. One of her friends brought a microphone to the hospital and put it on her bed. Every day, Kendall tried hard to pick it up with her right hand. It was more important for her to pick up that mic than a spoon or fork.Kendall is eighteen now, living every day to its fullest. She's recorded a CD with some of John Mellencamp's band members. She's also on CMT's Music City Madness for an original song and video, and is having some good success. I'm absolutely sure she's going to make it big some day. Kendall just puts it all in God's hands.I believe Kendall wanted the American Idol audition so much that she willed herself to move again. One of her friends brought a microphone to the hospital and put it on her bed. Every day, Kendall tried")
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
