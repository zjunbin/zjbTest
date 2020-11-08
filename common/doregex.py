#!-*-coding: utf-8 -*-
#!Time  : 2020/11/6 17:49
#!@Author : 张俊彬

import re
from common.readConfig import readConfig

conf = readConfig()

class contex:
    normal_user = conf.getother('test_user','normal_user')['user']
    normal_pwd = conf.getother('test_user','normal_user')['pwd']
    admin_user = conf.getother('test_user', 'admin_user')['user']
    admin_pwd = conf.getother('test_user', 'admin_user')['pwd']
    loanid_user = conf.getother('test_user', 'loanid_user')['user']
    loanid_pwd = conf.getother('test_user', 'loanid_user')['pwd']
    title = conf.getstr('project','title')
    amount = conf.getint('project','amount')

class DoRegex:
    def replace(self, data):
        res = re.findall('\$\{(.*?)\}', data)
        for item in res:
            value = getattr(contex, item)
            data = re.sub('\$\{(.*?)\}', value, data, count=1)
        return data
    def replace2(self,data):
        p = '\$\{(.*?)\}'
        while re.findall(pattern=p,string=data):
            data = re.sub(p,'repalace2',data,count=1)
        return data
if __name__ == '__main__':
    params = '{"mobilephone":"${phone}","pwd":"123456","regname":"${age}"}'
    p = "\$\{.+?\}"
    p2 = "\$\{(.*?)\}"
    res = re.findall(p,params)
    print(res)
    res2 = re.findall(p2,params)
    print(res2)
    # dr = DoRegex()
    # resp =dr.replace(params)
    # print(resp)
    # res = conf.getother('test_user','normal_user')['user']
    # print(res)
    # print(type(res))
    # setattr(contex,"COOKIES",'3234234')
    # if hasattr(contex,'cookies'):
    #     print('pass')
    # else:
    #     print('filed')
    data  = DoRegex().replace2(params)
    print(data)