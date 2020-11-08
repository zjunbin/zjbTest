#!-*-coding: utf-8 -*-
#!Time  : 2020/11/7 14:27
#!@Author : 张俊彬
import unittest
from cases.test_suite import suite
from HTMLTestRunnerNew import HTMLTestRunner
from common import constans
import sys
sys.path.append('./')
result_path = constans.result_path
with open(file=result_path, mode='wb+') as file:
    runner = HTMLTestRunner(file, 2, title='前程贷', description='接口测试', tester='lisa')
    runner.run(suite)
#测试