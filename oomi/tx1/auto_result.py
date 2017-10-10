# coding:utf-8
import smtplib
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpsetver=('smtp.163.com')

Sender=('tx77072@163.com')
psw=("tx12345678")
Receive=('770725462@qq.com')

file_name=r'C:\Users\Administrator.MICROSOFT\Desktop\messges\__pycache__\result.html'

msg = MIMEMultipart('related')
msg['from']=Sender
msg['to']=Receive
msg['subject']=file_name
text = MIMEText('自动化测试结果', 'plain', 'gbk')
msg.attach(text)
att = MIMEText(open(file_name, 'rb').read(), 'base64', 'gbk')
att["Content-Type"] = 'application/octet-stream'
att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', file_name))
msg.attach(att)


smtp=smtplib.SMTP()
smtp.connect(smtpsetver)
smtp.login(Sender,psw)
smtp.sendmail(Sender,Receive,msg.as_string())









