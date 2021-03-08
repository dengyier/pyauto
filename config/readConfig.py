'''
Create on:2020-12-10
@author: 麒麟
@email：dhb0113@163.com
    configparser模板是python中用于读取配置文件，通常情况下程序文件中的配置不能写死，方便灵活配置。
    readConfig.py 用于读取cfg.ini 文件中的配置，后续程序调用中，直接调用readConfig.py获取字段信息
'''

import os
import configparser

#定义变量config_path,配置文件路径
config_path = os.path.join(os.getcwd(),"config/cfg.ini")
#实例化ConfigParser方法
conf = configparser.ConfigParser()
conf.read(config_path)
#email 读取cfg.ini的字段信息
smtp_server = conf.get("email", "smtp_server")
porter = conf.get("email", "port")
send = conf.get("email", "sender")
pwd = conf.get("email", "password")
reciev = conf.get("email", "receiver")
#
# #Mysql 读取cfg.ini的字段信息
# host = conf.get("Mysql","host")
# mysql_port = conf.get("Mysql","My_port")
# user = conf.get("Mysql","user")
# passwd = conf.get("Mysql","My_password")
# db_name = conf.get("Mysql","db")
#

#读取命令行参数
cmdDevice = conf.get("command", "deviceCMD")
cmdInstall = conf.get("command", "installCMD")
cmdLog = conf.get("command", "logCMD")
cmdConn = conf.get("command", "connCMD")
cmdUi = conf.get("command", "uiCMD")
cmdPull = conf.get("command", "pullCMD")
cmdWait = conf.get("command", "waitCMD")
cmdTap = conf.get("command", "tapCMD")
cmdswipeUp = conf.get("command","swipeUpCMD")
cmdswipeDown = conf.get("command","swipeDownCMD")
cmdswipLeft = conf.get("command","swipLeftCMD")
cmdswipeRight = conf.get("command","swipRightCMD")
cmdBack = conf.get("command","backCMD")
