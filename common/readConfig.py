#!-*-coding: utf-8 -*-
#!Time  : 2020/11/6 15:44
#!@Author : 张俊彬
from configparser import ConfigParser
import os
from common import constans


class readConfig:
    def __init__(self):
        self.conf = ConfigParser()
        path = os.path.join(constans.config_path, 'global.conf')
        # 打开配置文件
        self.conf.read(filenames=path, encoding='utf-8')
        if self.conf.getboolean('swtich', 'on') == True:
            self.path = os.path.join(constans.config_path, 'online.conf')
            self.conf.read(filenames=self.path, encoding='utf-8')
        elif self.conf.getboolean('swtich', 'on') == False:
            self.path = os.path.join(constans.config_path, 'Test.conf')
            self.conf.read(filenames=self.path, encoding='utf-8')

    def getstr(self, section, option):
        value = self.conf.get(section=section, option=option)
        return value

    def getint(self, section, option):
        value = self.conf.getint(section=section, option=option)
        return value

    def getother(self, section, option):
        value = self.conf.get(section=section, option=option)
        return eval(value)

    def getfloat(self, section, option):
        value = self.conf.getfloat(section=section, option=option)
        return value

    def getboolean(self, section, option):
        value = self.conf.getboolean(section=section, option=option)
        return value

    def setvalue(self,section, option,value):
        self.conf.set(section=section,option=option,value=value)
        with open(self.path, 'w+', encoding='utf-8') as f:
            self.conf.write(f)



if __name__ == '__main__':
    read = readConfig()
    read.setvalue('register_phone', 'phone','18916666778')
    res  = read.getstr('register_phone', 'phone')
    print(res)
    print(type(res))
