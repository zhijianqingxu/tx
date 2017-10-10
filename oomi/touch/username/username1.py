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
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(10)





    def test02(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').send_keys('ass')
        self.test01()
    def test03(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').send_keys(123)
        self.test01()
    def test04(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').send_keys('qw')
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').send_keys(1234)
        self.test01()


    def test05(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').send_keys('qw')
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_btn_ok').click()
        time.sleep(10)



    def test06(self):
        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        x1 = int(x['width'] * 0.93)
        y1 = int(y['height'] * 0.27)
        self.driver.tap([(x1, y1), ])
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_btn_logout').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_btn_logout').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(20)


    def test07(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_forgotpassword').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_ok').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()


    def test08(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').clear()

        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').send_keys('qwerdadfggggh')

        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_ok').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
    def test09(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').send_keys('wertedsa1234sdefghjgfda12ezawqded@qq.com')



        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_ok').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

    def test10(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').send_keys('jj.jj_k1554-hi44@qq.com')

        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_ok').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

    def test11(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').send_keys(
            '770725462@qq.com')

        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_ok').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()

    def test12(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_email').send_keys(
            'OO@qq.com')

        self.driver.find_element_by_id('com.fantem.launcher:id/forgot_password_ok').click()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/back').click()
        time.sleep(5)

    def test13(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_signup').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)

    def test14(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('asdfg')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
    def test15(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('qwerfds@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
    def test16(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys('asdf')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
    def test17(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys('asdfg')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)


    def test18(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qw')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('adfx@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)

    def test19(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qfzw.xedcrfvtgbyhn12')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('faaf@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)


    def test20(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qazadawccz')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('weraedsa1234daefghjgfda12ezawqded@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)

    def test21(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qazwccz')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
    def test22(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qafdcz')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('werawqded@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
    def test23(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qazadcz')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('weraeqded@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
        time.sleep(3)
    def test24(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('qadadaad')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('wead1234afafcqded@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys('d-s12.ww_2d4zec')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys('d-s12.ww_2d4zec')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
    def test25(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('~方法!@#$%^&*()')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('~!#$方法%^&*()')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys('~!#方法$%^&*()')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(
            '~!#$%^&*()')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)

    def test26(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('rva')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('770725462@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)

    def test27(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_username').send_keys('rffva')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_email').send_keys('77ffaf0725462@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_password').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_confirmpassword').send_keys(2)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/signup_activity_back').click()

    def test28(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').send_keys('770725462@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_btn_ok').click()
        time.sleep(10)

    def test29(self):
        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        x1 = int(x['width'] * 0.93)
        y1 = int(y['height'] * 0.27)
        self.driver.tap([(x1, y1), ])
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_btn_logout').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_btn_logout').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(20)

    def test30(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').send_keys('weraedsa1234daefghjgfda12ezawqded@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_btn_ok').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        time.sleep(10)


    def test31(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_username').send_keys('770725462@qq.com')
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_userpassword').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/login_activity_btn_ok').click()
        time.sleep(10)

    def test32(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfo_textView_country').click()
        self.driver.find_element_by_name('阿尔巴尼亚').click()
        self.driver.find_element_by_name('阿尔及利亚').click()
        self.driver.find_element_by_name('阿富汗').click()
        self.driver.find_element_by_name('阿尔巴尼亚').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/set_country_activity_back').click()
        time.sleep(10)

    def test33(self):
        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        x1 = int(x['width'] * 0.93)
        y1 = int(y['height'] * 0.27)
        self.driver.tap([(x1, y1), ])
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_relativeLayout_password').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_relativeLayout_password').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
    def test34(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').send_keys('da')
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').clear()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').send_keys('dad')
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').clear()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').send_keys('dadzz')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)



    def test35(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').send_keys('daxz')
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').send_keys('dxz')
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
    def test36(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').send_keys('daxz')
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').send_keys('fafag')
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').clear()

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
    def test37(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').send_keys('fafaf')

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
    def test38(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').send_keys('fafag.13-da_4axfxze1')
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').send_keys('fafag.13-da_4axfxze1')


        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)

    def test39(self):
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_relativeLayout_password').click()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_old').send_keys('fafag.13-da_4axfxze1')
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_new').send_keys(1)
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').clear()
        self.driver.find_element_by_id('com.fantem.launcher:id/dialog_editpassword_confirm').send_keys(1)

        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.fantem.launcher:id/userinfoalter_imageView_back').click()

    def test40(self):
        if True:
            t1=self.driver.find_element_by_name('绑定Cube').text
            t1==('绑定Cube')
            self.driver.find_element_by_id('com.fantem.launcher:id/btn_user_bind_cube').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('com.fantem.launcher:id/bt_cancel').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('com.fantem.launcher:id/btn_user_bind_cube').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
            time.sleep(5)
            self.driver.find_element_by_id('com.fantem.launcher:id/bt_ok').click()
        else:
            pass




    @classmethod
    def tearDownClass(cls):
            cls.driver.quit()

if __name__ == '__main__':
        unittest.main()






















