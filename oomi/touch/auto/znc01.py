#coding:utf-8
import unittest
import appium
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
class Testtx(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tx = {}
        tx['platformName'] = ('Android')
        tx['plaformVersion'] = ('4.4.4')
        tx['deviceName'] = ('A010116390040029')
        tx['appPackage'] = ('com.fantem.launcher')
        # tx['app']=('C:\\qw\\OOMI.apk')
        tx['appActivity'] = ('com.fantem.launcher.StartActivity')
        tx['appWaitActivity'] = ('com.fantem.launcher.StartActivity')
        tx['unicodeKeyboard'] = ('True')
        tx['resetKeyboard'] = ('True')
        cls.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',tx)
        time.sleep(20)
        cls.driver.find_element_by_id("com.fantem.launcher:id/left_menu").click()

    def test(self):
        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        x1 = int(x['width'] * 0.38)
        y1 = int(y['height'] * 0.31)
        self.driver.tap([(x1, y1), ])
        time.sleep(10)


        x2 = int(x['width'] * 0.52)
        x3 = int(x['width'] * 0.72)
        y2 = int(y['height'] * 0.99)
        y3 = int(y['height'] * 0.27)
        for i in range(1, 2):
            self.driver.swipe(x2, y2, x3, y3, 1000)
            self.driver.implicitly_wait(10)
            print(i)
        time.sleep(10)



    def test1(self):
        for pp in range(1,4):
            self.driver.find_element_by_id('com.fantem.launcher:id/rsi_right_add').click()
            self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys('qwert1234._()/哈哈23jk')
            self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
            print(pp)
            time.sleep(20)
            self.driver.find_element_by_id('com.fantem.launcher:id/back_control_activity').click()
            self.test()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()



