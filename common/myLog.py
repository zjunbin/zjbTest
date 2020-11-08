#!-*-coding: utf-8 -*-
#!Time  : 2020/11/6 15:44
#!@Author : 张俊彬
import logging
import os
import time
from common.readConfig import readConfig
from common import constans


rf = readConfig()

class MyLog:
    def __init__(self,loggername):
        self.loggername = loggername
        self.logger_level = rf.getstr('testconfig','logger_level').upper()
        self.formatter_set = rf.getstr('testconfig','formatter')
        self.srteam_level = rf.getstr('testconfig','srteam_level').upper()
        self.file_level = rf.getstr('testconfig','file_level').upper()

    def myLog(self, level, msg):
        logger = logging.getLogger(self.loggername)
        # 设置日志收集级别
        logger.setLevel(level=self.logger_level)
        # 日志输出的格式
        formatter = logging.Formatter(self.formatter_set)
        ch = logging.StreamHandler()  # 渠道输出到控制台
        ch.setLevel(self.srteam_level) #控制台输出级别
        ch.setFormatter(formatter)
        path = constans.log_path
        if not os.path.exists(path):
            os.mkdir(path)
        day = time.strftime("%Y-%m-%d")
        fh = logging.FileHandler(constans.log_path+ "/" + day + ".log", encoding="UTF-8")  # 渠道输出到文件
        fh.setLevel(self.file_level) #文件输出级别
        fh.setFormatter(formatter)
        # 对接
        logger.addHandler(ch) #输出到控制台渠道
        logger.addHandler(fh) #输出到文件渠道
        if level.upper() == "DEBUG":
            logger.debug(msg=msg)
        elif level.upper() == "INFO":
            logger.info(msg=msg)
        elif level.upper() == "WARNING":
            logger.warning(msg=msg)
        elif level.upper() == "ERROR":
            logger.error(msg=msg)
        elif level.upper() == "CRITICAL":
            logger.critical(msg=msg)
        #使用完成移除
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.myLog(msg=msg, level='debug')

    def info(self, msg):
        self.myLog(msg=msg, level='info')

    def warning(self, msg):
        self.myLog(msg=msg, level='warning')

    def error(self, msg):
        self.myLog(msg=msg, level='error')

    def critical(self, msg):
        self.myLog(msg=msg, level='critical')
if __name__ == '__main__':
    mylog = MyLog('dd')
    mylog.debug('dafd')