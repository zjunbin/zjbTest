#!-*-coding: utf-8 -*-
#!Time  : 2020/11/6 20:50
#!@Author : 张俊彬
from common.readConfig import readConfig
import os
import requests
# par = {"mobilephone":"phone","pwd":"123456","regname":"小名"}
# print(type(par))
#
# if par['mobilephone'] == 'phone':
#     par['mobilephone'] = 123123123
# print(par)
data = {"mobilephone":"13822221111","pwd":"123456"}
url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
resp = requests.post(url,data)
url2 = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
data2 = {"mobilephone":"13822221113","amount":"1"}
re = requests.post(url=url2,data=data2,cookies = resp.cookies)
print(re.json())
print(re.text)

# read_path = readConfig().getstr(section='url',option='url')
# item = {'url':'/member/register'}
# url = os.path.join(read_path ,item['url'])
# print(url)

# a = 'dc baa'
# res  = a.find('a')
# print(res)