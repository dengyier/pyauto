'''
Create on:2020-01-12
@author: 十三先生
@email：haibod@jumei.com
    run_all_case是一个执行所有测试用例的执行方法
'''

import smtplib
import unittest
import os
import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from config.readConfig import *
from common.logConf import Logs

def all_case():
    #定义用例存放目录
    case_dir = os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    #使用discover方法加载所有的测试用例
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)

    for test_suit in discover:
        for test_case in test_suit:
            testcase.addTests(test_case)
    print(testcase)

    return testcase

def send_mail(file_new):

    smtpserver = smtp_server
    port = porter
    sender = send
    password = pwd
    reciever = reciev

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    body = MIMEText(mail_body,'html','utf-8')
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化报告","utf-8").encode()
    msg['From'] = sender
    msg['To'] = Header(u'负责人 <%s>' %reciever)
    msg['To'] = ';'.join(reciever)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)

    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.ehlo()  #确认身份
        smtp.starttls()
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port,timeout=300)
        smtp.login(sender, password)  # 登录
    smtp.sendmail(sender, reciever, msg.as_string())  # 发送
    smtp.quit()

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    log = Logs()  #调用Logs函数
    log.info("-------测试开始--------")
    log.info("状态已开启，请开始你的表演")
    #开启unittest用例执行方法
    runner = unittest.TextTestRunner()
    timesheet = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    report_path = os.path.join(os.getcwd(),"report/report-"+timesheet+".html")   #报告路径
    fp = open(report_path,'wb')
    #调取HTMLTestRunner方法
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"这是我的自动化用例",description=u"用例执行情况",verbosity=2)
    runner.run(all_case())
    fp.close()
    test_path = os.path.join(os.getcwd(),"report")
    new_report=new_report(test_path)
    send_mail(new_report)#发送邮件
    log.warning("------测试结束------")