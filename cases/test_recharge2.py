#!-*-coding: utf-8 -*-
#!Time  : 2020/11/7 15:17
#!@Author : 张俊彬
import unittest,json
from ddt import ddt,data
from common.http_requests import Request
from common.doregex import contex,DoRegex
from common import constans
from common.readConfig import readConfig
from common.readExcel import readExcel
from common.myLog import MyLog

red = readExcel(filename=constans.data_case, sheetname='recharge')
data_case = red.do_excel()

@ddt
class TestRecharge(unittest.TestCase):
    def setUp(self):
        self.read_path = readConfig().getstr(section='url', option='url')
        self.rc = readConfig()
        self.mylog = MyLog('recharge模块')

    @data(*data_case)
    def test_recharge(self,item):
        '''通过反射查看是否有COOKIES的值'''
        if hasattr(contex, 'COOKIES'):
            COOKIES = getattr(contex, 'COOKIES')
        else:
            COOKIES = None
        print('COOKIES:',COOKIES)
        params = json.loads(DoRegex().replace(item['params']))
        url = self.read_path + item['url']
        resp = Request(url=url,method=item['method'],data=params,cookies=COOKIES)
        if resp.cookies():
            setattr(contex,'COOKIES',resp.cookies())
        actual = resp.get_txt()
        try:
            self.assertEqual(actual, item['excepted'])
            self.mylog.debug('正在执行第{}个用例，测试参数: {},测试结果：{}'.format(item['caseid'], params, actual))
            result = 'Pass'
        except AssertionError as e:
            result = 'Filed'
            self.mylog.error('正在执行第{}个用例，测试参数: {},断言结果：{}'.format(item['caseid'], params, e))
            raise e
        finally:
            red.write_back(row=item['caseid'] + 1, column=7, value=actual)
            red.write_back(row=item['caseid'] + 1, column=8, value=result)