# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(smtpHost, smtpPort, sendAddr, password, recipientAddrs, attach, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件，传送D:/软件/yasuo.rar文件
    if attach:
        print('attach')
        part = MIMEApplication(open("./books/"+attach, 'rb').read())
        part.add_header('Content-Disposition', 'attachment',
                        filename=attach[attach.find('/'):])
        msg.attach(part)
    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, smtpPort)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()
