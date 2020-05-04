# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/4/30 12:59
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from configparser import ConfigParser
from config.get_path import *

class GetMail():
    def mail_data(self):
        cp = ConfigParser()
        cp.read(mail_path)
        server = cp.get('mail','smtp_server')
        sender = cp.get('mail','smtp_sender')
        pawssword = cp.get('mail','smtp_pawssword')
        receiver = cp.get('mail','smtp_receiver')

        mm = MIMEMultipart()
        mm['Subject'] = '来自大大美女的一封信'  # 邮件主题
        mm['From'] = sender  # 发送人
        mm['To'] = receiver  # 接收人



        # 获取最新的HTML文件
        lists= os.listdir(html_path)
        new_html = os.path.join(html_path,lists[-1])

        f = open(new_html,'rb')
        mail_body= f.read()
        f.close()

        content = MIMEText(mail_body,'html','utf-8')  # 添加正文
        mm.attach(content)

        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        mm.attach(att)

        # smtp = smtplib.SMTP()
        # smtp.connect(server)
        # smtp.login(sender,pawssword)
        # smtp.send_message(mm)
        # smtp.quit()