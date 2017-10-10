# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import unittest


class Testmessges(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        cls.driver = webdriver.Chrome(chrome_options=options)

        cls.driver.get("https://testadmin.fantem-gateway.com/#/account/account_login")
        cls.driver.implicitly_wait(20)


        cls.driver.find_element_by_id('username').send_keys('qw')
        cls.driver.find_element_by_id('password').send_keys(1)
        cls.driver.find_element_by_xpath("html/body/app-layout/div/div/div/div/div/form/div[5]/div/input").click()

        cls.driver.find_element_by_xpath(
            "html/body/app-layout/div/div/div[1]/layout-menu/div/accordion/div/div[5]/div[1]/h4/a/span").click()
        time.sleep(5)
        cls.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[1]/layout-menu/div/accordion/div/div[5]/div[2]/div/ul/li[1]/a").click()

    def test01(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys('Hello, oomi. Welcome to this big family！')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('Hello, oomi. Welcome to this big family！')
        self.driver.find_element_by_xpath('//*[@id="_Ios"]').click()
        self.driver.find_element_by_xpath("//*[@id='_Ios_User']").click()
        try:
            t1=self.driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/form/div[10]/div/div/label/input")
        except NoSuchElementException as msg:
            print('查找异常元素%s' % msg)
        else:
            self.driver.find_element_by_xpath(
                "/html/body/app-layout/div/div/div[2]/div/div/form/div[10]/div/div/label/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()

        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test01')

    def test02(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys('Hello, oomi. Welcome to this big family！')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('Hello, oomi. Welcome to this big family！')
        self.driver.find_element_by_xpath("//*[@id='_Android']").click()
        self.driver.find_element_by_xpath("//*[@id='_Android_User']").click()
        try:
            t1=self.driver.find_element_by_xpath("/html/body/app-layout/div/div/div[2]/div/div/form/div[8]/div/div[2]/label/input")
        except NoSuchElementException as msg:
            print('查找异常元素%s'%msg)
        else:
            self.driver.find_element_by_xpath(
                "/html/body/app-layout/div/div/div[2]/div/div/form/div[8]/div/div[2]/label/input").click()

        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test02')

    def test03(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys('Hello, oomi. Welcome to this big family')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('Hello, oomi. Welcome to this big family')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_id('_Touch_User').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').click()
        self.driver.find_element_by_id('_pushTimeNow').click()
        self.driver.find_element_by_id('_MessageTypeC').click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)

        self.driver.find_element_by_xpath("html/body/app-layout/div/div/div[2]/div/div/form/div[15]/div/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test03')

    def test04(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(
            'html/body/app-layout/div/div/div[1]/layout-menu/div/accordion/div/div[5]/div[2]/div/ul/li[1]/a').click()
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'touch 丰唐123！#@￥%…&*（）{}|“”：《》？~+和聽到的..吔吥一定會是眞的... Ngáje Ngái')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'touch 丰唐123！#@￥%…&*（）{}|“”：《》？~+和聽到的..吔吥一定會是眞的... Ngáje Ngái')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
        time.sleep(5)
        if True:
            tr = self.driver.find_element_by_xpath(
                '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').is_selected()
            pass
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test04')

    def test05(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()

        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys('刚进入NBA的时候,很多人认为他只是一个角色球员.')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            '刚进入NBA的时候,很多人认为他只是一个角色球员,很难生存下去.后来,人们觉得他有可能成为球队首发.又过了一段时间,他成为了全明星.到最后,他成为了篮球史上的超级巨星.　2017年,人们称李卫为篮球皇帝,王朝教父,史上最伟大的球员和教练,超越神的男人,穿着球衣的上帝,是他,让邓肯')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
        time.sleep(5)
        if True:
            tr = self.driver.find_element_by_xpath(
                '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').is_selected()
            pass
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath("//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test05')

    def test06(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            "I believe Kendall wanted the American Idol audition so much that she willed herself to move again. One of her friends bro")
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            "I believe Kendall wanted the American Idol audition so much that she willed herself to move again. One of her friends brought a microphone to the hospital and put it on her bed. Every day, Kendall tried hard to pick it up with her right hand. It was more important for her to pick up that mic than a spoon or fork.Kendall is eighteen now, living every day to its fullest. She's recorded a CD with some of John Mellencamp's band members. She's also on CMT's Music City Madness for an original song and video, and is having some good success. I'm absolutely sure she's going to make it big some day. Kendall just puts it all in God's hands.I believe Kendall wanted the American Idol audition so much that she willed herself to move again. One of her friends brought a microphone to the hospital and put it on her bed. Every day, Kendall tried")
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
        time.sleep(5)
        if True:
            tr = self.driver.find_element_by_xpath(
                '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').is_selected()
            pass
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath("//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test06')

    def test07(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys('delayed')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('delayed')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
        time.sleep(5)
        if True:
            tr = self.driver.find_element_by_xpath(
                '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').is_selected()
            pass
        self.driver.find_element_by_xpath("//*[@id='_pushTime']").click()
        js = 'document.getElementById("dtp_input1").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.driver.find_element_by_id("dtp_input1").clear()
        self.driver.find_element_by_id("dtp_input1").send_keys("2017-09-28 16:00:00")

        time.sleep(3)
        self.driver.find_element_by_id("_title").click()
        self.driver.find_element_by_xpath("//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test07')

    def test08(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys('yanshi30')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys('yanshi30')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
        time.sleep(5)
        if True:
            tr = self.driver.find_element_by_xpath(
                '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').is_selected()
            pass
        self.driver.find_element_by_xpath("//*[@id='_pushTimeDelay']").click()
        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[11]/div/label[4]/input").send_keys('30')
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test08')

    def test09(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'There is an upgrade package. Do you need to upgrade?')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'There is an upgrade package. Do you need to upgrade?')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath("//*[@id='_Touch_User']").click()
        time.sleep(5)
        if True:
            tr = self.driver.find_element_by_xpath(
                '/html/body/app-layout/div/div/div[2]/div/div/form/div[6]/div/div[9]/label/input').is_selected()
            pass
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath("//*[@id='_MessageTypeO']").click()
        self.driver.find_element_by_xpath("//*[@id='touchOTA']").click()
        js = ('window.scrollTo(0,document.body.scrollHeight)')
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test09')

    def test10(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！All Touch Client')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！All Touch Client')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[5]/div/label[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test10')

    def test11(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！All Touch User')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！All Touch User')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[5]/div/label[2]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test11')

    def test12(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！alphar')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！alphar')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[5]/div/label[3]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test12')

    def test13(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！beta')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！beta')
        self.driver.find_element_by_xpath(".//*[@id='_Touch']").click()
        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[5]/div/label[4]/input").click()

        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test13')

    def test14(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！beta')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！beta')
        self.driver.find_element_by_xpath("//*[@id='_Android']").click()
        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[7]/div/label[4]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()
        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test14')

    def test15(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！alphar ')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！alphar ')
        self.driver.find_element_by_xpath("//*[@id='_Android']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[7]/div/label[3]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test15')

    def test16(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！All Android User')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！All Android User')
        self.driver.find_element_by_xpath("//*[@id='_Android']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[7]/div/label[2]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test16')

    def test17(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！All Android Client')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！All Android Client')
        self.driver.find_element_by_xpath("//*[@id='_Android']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[7]/div/label[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test17')

    def test18(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！alphar')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！alphar')
        self.driver.find_element_by_xpath('//*[@id="_Ios"]').click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[9]/div/label[3]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test18')

    def test19(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！beta')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！beta')

        self.driver.find_element_by_xpath('//*[@id="_Ios"]').click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[9]/div/label[4]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test19')

    def test20(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！All IOS Client ')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！All IOS Client ')
        self.driver.find_element_by_xpath('//*[@id="_Ios"]').click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[9]/div/label[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test20')

    def test21(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！All IOS User ')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！All IOS User ')
        self.driver.find_element_by_xpath('//*[@id="_Ios"]').click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[9]/div/label[2]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test21')

    def test22(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！_All User_Gamma')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！_All User_Gamma')
        self.driver.find_element_by_xpath("//*[@id='_All_User']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[4]/div/label[3]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test22')

    def test23(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！_All User_Beta')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！_All User_Beta')
        self.driver.find_element_by_xpath("//*[@id='_All_User']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[4]/div/label[2]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test23')

    def test24(self):
        self.driver.find_element_by_xpath(".//*[@id='_title']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_title']").send_keys(
            'Hello, oomi. Welcome to this big family！_All User_Alpha')
        self.driver.find_element_by_xpath(".//*[@id='_massage']").clear()
        self.driver.find_element_by_xpath(".//*[@id='_massage']").send_keys(
            'Hello, oomi. Welcome to this big family！_All User_Alpha')
        self.driver.find_element_by_xpath("//*[@id='_All_User']").click()

        self.driver.find_element_by_xpath(
            "/html/body/app-layout/div/div/div[2]/div/div/form/div[4]/div/label[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='_pushTimeNow']").click()
        self.driver.find_element_by_xpath(".//*[@id='_MessageTypeC']").click()

        self.driver.find_element_by_xpath('//app-layout/div/div/div[2]/div/div/form/div[15]/div/button').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').send_keys(Keys.TAB)
        t1 = self.driver.find_element_by_xpath('//*[@id="_model"]').text
        if t1 == ('推送成功'):
            print('推送成功')
        elif t1 == ('推送失败'):
            print('推送失败')
        else:
            print('错误')

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button').click()
        time.sleep(5)
        print('test24')

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()


