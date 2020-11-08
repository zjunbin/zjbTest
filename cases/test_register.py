#!-*-coding: utf-8 -*-
#!Time  : 2020/11/6 17:13
#!@Author : 张俊彬
import json
import unittest
import os
from ddt import ddt,data
from common.http_requests import Request
from common.readExcel import readExcel
from common import constans
from common.readConfig import readConfig
from common.myLog import MyLog

red = readExcel(filename=constans.data_case, sheetname='register')
data_case = red.do_excel()

@ddt
class TestRegister(unittest.TestCase):
    def setUp(self):
        self.rc = readConfig()
        self.read_path = self.rc.getstr(section='url', option='url')
        self.mylog = MyLog('register模块')


    @data(*data_case)
    def test_register(self,item):
        params = json.loads(item['params'])
        value = self.rc.getstr(section='register_phone', option='phone')
        if params['mobilephone'] == 'phone':
            params['mobilephone'] = value
        url = self.read_path + item['url']
        res = Request(method=item['method'], url=url, data=params)
        actual = res.get_txt()
        resp = res.get_json()
        try:
            self.assertEqual(actual, item['excepted'])
            if resp['msg'] == '注册成功':
                self.rc.setvalue('register_phone','phone',value=str(int(value)+1))
            result = 'Pass'
            self.mylog.debug('正在执行第{}个用例，测试参数: {},测试结果：{}'.format(item['caseid'],params,resp))
        except Exception as e:
            result = 'Filed'
            self.mylog.error('正在执行第{}个用例，测试参数: {},断言结果：{}'.format(item['caseid'], params, e))
            raise e
        finally:
            red.write_back(item['caseid']+1, 7,actual)
            red.write_back(item['caseid']+1 ,8,result)

