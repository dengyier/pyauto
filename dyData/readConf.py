
import os
import configparser


#定义变量config_path,配置文件路径
# config_path = os.path.join(os.getcwd(),"dyData/cnf.ini")
#实例化ConfigParser方法
conf = configparser.ConfigParser()
# conf.read(config_path)
conf.read('.%scnf.ini' % os.path.sep)
#读取config.ini的字段信息

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

