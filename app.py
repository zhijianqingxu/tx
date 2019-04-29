#coding:utf-8
from  appium import  webdriver
from time import sleep
desired_caps = {

                'platformName': 'Android',

                'deviceName': '127.0.0.1:62001',

                'platformVersion': '5.1',

                # apk包名

                'appPackage': 'com.tuya.smart',

                # apk的launcherActivity

                'appActivity': 'com.tuyasmart.sample.TuyaSplashActivity'

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)
driver.find_element_by_id('com.tuya.smart:id/btn_login').click()
driver.find_element_by_name(r'手机号 / 邮箱').send_keys('18027661321')
driver.find_element_by_xpath('//android.widget.TextView[@content-desc=\"login_pw\"]').send_keys('qw12345678')

driver.find_element_by_xpath('//android.widget.TextView[@text=\"登录\" and @content-desc=\"login_login\"]').click()
sleep(5)

driver.find_element_by_id('com.tuya.smart:id/iv_room_set').click()
sleep(1)
driver.find_element_by_name('添加房间').click()
sleep(1)
driver.find_element_by_name('客厅').click()
sleep(1)
driver.find_element_by_name('完成').click()
sleep(1)
driver.find_element_by_name('编辑').click()
sleep(1)
driver.find_element_by_id('com.tuya.smart:id/iv_remove').click()
driver.find_element_by_name('确认删除').click()
driver.find_element_by_class_name('android.widget.ImageButton').click()
driver.find_element_by_class_name('android.widget.ImageButton').click()
sleep(1)
driver.find_element_by_name('我').click()
sleep(1)
driver.find_element_by_name('设置').click()
sleep(1)
driver.find_element_by_name('退出登录').click()
sleep(1)

driver.quit()