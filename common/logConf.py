'''
Create on:2020-12-10
@author: 麒麟
@email：dhb0113@163.com
    logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等，可以通过
设置不同的日志等级，在release版本中只输出重要信息，而不必显示大量的调试信息。
'''
import logging,time
import os
#定义log_path，日志路径变量
log_path = os.path.join(os.getcwd(),'logs')
if not os.path.exists(log_path): os.mkdir(log_path)
#定义一个Class
class Logs():
    #构造函数初始化
    def __init__(self):
        self.logName = os.path.join(log_path,'%s.log'%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
    # 定义一个私有方法
    def __console(self,level,message):
        #创建FileHandler,写入本地
        fl = logging.FileHandler(self.logName,'a',encoding='utf-8')
        fl.setLevel(logging.DEBUG)
        fl.setFormatter(self.formatter)
        self.logger.addHandler(fl)

        #创建SteamHandler,用于输出到工作台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        #判断level级别
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fl)
        #关闭打开的文件
        fl.close()
    #封装debug方法
    def debug(self,message):
        self.__console('debug',message)

    #封装info方法
    def info(self,message):
        self.__console('info',message)
    #封装warning方法
    def warning(self,message):
        self.__console('warning',message)
    #封装error方法
    def error(self,message):
        self.__console('error',message)







