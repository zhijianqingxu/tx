
#coding:utf-8
#import unittest
#import HTMLTestRunner
#import io
#case_path=r'E:\\tx\\tx'
#def all_case():
 #   discover = unittest.defaultTestLoader.discover(case_path,
   #                                                 pattern="message*.py",
    #                                                top_level_dir=None)
  #  print(discover)
    #return discover
#if __name__=='__main__':
   #report_path=r"E:\tx\tx\result.html"
   #fp=open(report_path,'wb')
   #runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                    title="自动化测试结果",
     #                                   description='结果')
   #runner.run(all_case())







#coding:utf-8
import smtplib
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
import HTMLTestRunner
import io
case_path=r'E:\tx\tx'
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="message*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover
if __name__=='__main__':
   report_path=r"E:\tx\tx\result.html"
   fp=open(report_path,'wb')
   runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                        title="自动化测试结果",
                                        description='结果')
   runner.run(all_case())












smtpsetver=('smtp.163.com')

Sender=('tx77072@163.com')
psw=("tx12345678")
Receive=('770725462@qq.com')

file_name=r'E:\tx\tx\result.html'

msg = MIMEMultipart('related')
msg['from']=Sender
msg['to']=Receive
msg['subject']=file_name
text = MIMEText('result', 'plain', 'gbk')
msg.attach(text)
att = MIMEText(open(file_name, 'rb').read(), 'base64', 'gbk')
att["Content-Type"] = 'application/octet-stream'
att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', file_name))
msg.attach(att)


smtp=smtplib.SMTP()
smtp.connect(smtpsetver)
smtp.login(Sender,psw)
smtp.sendmail(Sender,Receive,msg.as_string())









