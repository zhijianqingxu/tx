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
        x2 = int(x['width'] * 0.1)
        x3 = int(x['width'] * 0.3)
        y2 = int(y['height'] * 0.99)
        y3 = int(y['height'] * 0.27)
        for i in range(1, 5):
            self.driver.swipe(x2, y2, x3, y3, 1000)
            self.driver.implicitly_wait(10)
            print(i)
        time.sleep(10)




    def test01(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys(
            'qwrtyu.iop_/()解决123')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(20)

        if True:
            self.driver.find_element_by_name('超时')

            self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        else:
            pass



        time.sleep(3)
        self.test()

    def test02(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys(
            '丰唐物联科技有限公司丰唐物联科技有限公司')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

        time.sleep(10)
        self.test()

    def test03(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys(
            'qwertyuiopasdfghjklz')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

        time.sleep(10)
        self.test()
    def test04(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/set_select').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys(
            'qwedacj1235456')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

        time.sleep(10)
        self.test()
    def test05(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        t1=self.driver.find_element_by_name('请输入名称').text
        t2=('请输入名称')
        self.assertEqual(t1,t2)
        print('不为空')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/set_select').click()
    def test06(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys(
            '~!@#^-()_+:<>?')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

        time.sleep(10)
        self.test()
    def test07(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/tv_add').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys(
            '1234567890qwertyuiop1')
        time.sleep(3)
        t1=self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').text
        len(t1)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

        time.sleep(10)
        self.driver.find_element_by_id('com.fantem.launcher:id/set_select').click()
        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        x1 = int(x['width'] * 0.1)
        y1 = int(y['height'] * 0.31)
        self.driver.tap([(x1, y1), ])
        time.sleep(5)
        x2 = int(x['width'] * 0.14)
        x3 = int(x['width'] * 0.14)
        y2 = int(y['height'] * 0.31)
        y3 = int(y['height'] * 0.76)
        for i in range(1, 5):
            self.driver.swipe(x2, y2, x3, y3, 1000)
            self.driver.implicitly_wait(10)

        time.sleep(5)


    def test08(self):

        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys('awafafaf')
        time.sleep(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(10)

    def test09(self):
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/updatedevicesandroos_edt_content').send_keys('oinnncz()/kk_')
        time.sleep(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(10)

    def test10(self):
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
    def test11(self):
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[2]/android.widget.ImageView[2]').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id=\"com.fantem.launcher:id/left_room\"]/android.widget.RelativeLayout[2]/android.widget.ImageView[2]').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/set_select').click()




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()



