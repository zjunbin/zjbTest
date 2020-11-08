#!-*-coding: utf-8 -*-
# !Time  : 2020/11/6 15:49
# !@Author : 张俊彬
import os

import time

day = time.strftime("%Y-%m-%d")
# 项目根目录
path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 全局配置文件路径
globals_path = os.path.join(path, 'config')
# config 配置文件目录
config_path = os.path.join(path, 'config')
# 日志输出路径和名称
log_path = os.path.join(path, 'logs/')
# 测试用例存放路径和名称
data_case = os.path.join(path, 'datas', 'testcase.xlsx')
# 测试报告存放
result_path = os.path.join(path, 'result' + '/' + day + '-result.html')

if __name__ == '__main__':
    print(log_path)
