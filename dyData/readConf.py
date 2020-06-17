
import os
import configparser


#定义变量config_path,配置文件路径
# config_path = os.path.join(os.getcwd(),"dyData/cnf.ini")
#实例化ConfigParser方法
conf = configparser.ConfigParser()
# conf.read(config_path)
conf.read('/Users/yaoyao/Learn/dyData/cnf.ini')
#读取config.ini的字段信息

cmdDevice = conf.get("command", "deviceCMD")
cmdInstall = conf.get("command", "installCMD")
cmdLog = conf.get("command", "logCMD")
cmdConn = conf.get("command", "connCMD")
cmdUi = conf.get("command", "uiCMD")
cmdPull = conf.get("command", "pullCMD")
cmdWait = conf.get("command", "waitCMD")
cmdTap = conf.get("command", "tapCMD")

