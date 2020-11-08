#!-*-coding: utf-8 -*-
#!Time  : 2020/11/7 14:24
#!@Author : 张俊彬
import unittest
from cases.test_login import TestLogin
from cases.test_register import TestRegister
from cases.test_recharge import TestRecharge

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLogin))
suite.addTest(loader.loadTestsFromTestCase(TestRegister))
suite.addTest(loader.loadTestsFromTestCase(TestRecharge))
# 测试数据