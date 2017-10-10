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
        time.sleep(10)
        cls.driver.find_element_by_id("com.fantem.launcher:id/left_menu").click()

    def test(self):

        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        x1 = int(x['width'] * 0.37)
        y1 = int(y['height'] * 0.75)
        self.driver.tap([(x1, y1), ])
        self.driver.tap([(x1, y1), ])
        time.sleep(10)
        #self.driver.find_element_by_id('com.fantem.launcher:id/set_select').click()
        '''


        x2 = int(x['width'] * 0.52)
        x3 = int(x['width'] * 0.72)
        y2 = int(y['height'] * 0.99)
        y3 = int(y['height'] * 0.27)
        for i in range(1, 2):
            self.driver.swipe(x2, y2, x3, y3, 1000)
            self.driver.implicitly_wait(10)
            print(i)
        time.sleep(10)
        '''
    def test01(self):
        self.driver.find_element_by_name('单位').click()
        for i  in range(1,8):
            self.driver.find_element_by_name('湿度').click()
            print(i)
        for o in range(1,8):
            self.driver.find_element_by_name('距离').click()
        time.sleep(5)



    @classmethod
    def tearDownClass(cls):
            cls.driver.quit()

if __name__ == '__main__':
        unittest.main()



