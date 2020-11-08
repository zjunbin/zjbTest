#!-*-coding: utf-8 -*-
# !Time  : 2020/11/7 13:32
# !@Author : 张俊彬
import unittest, json
from ddt import ddt, data
from common.http_requests import Request
from common.readExcel import readExcel
from common import constans
from common.readConfig import readConfig
from common.myLog import MyLog
from common.doregex import contex, DoRegex

filepath = constans.data_case

re = readExcel(filename=filepath, sheetname='login')
data_case = re.do_excel()


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.mylog = MyLog('login模块测试')

    @data(*data_case)
    def test_logig(self, item):
        params = json.loads(DoRegex().replace(data=item['params']))
        url = readConfig().getstr('url', 'url') + item['url']
        resp = Request(url=url, method=item['method'], data=params)
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
            re.write_back(row=item['caseid'] + 1, column=7, value=actual)
            re.write_back(row=item['caseid'] + 1, column=8, value=result)
