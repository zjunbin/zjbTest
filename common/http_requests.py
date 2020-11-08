#!-*-coding: utf-8 -*-
#!Time  : 2020/11/6 16:57
#!@Author : 张俊彬
import requests
from common.myLog import MyLog


class Request:
    def __init__(self, method, url, data, cookies = None):
        mylog = MyLog('Request请求')
        if method.upper() == 'GET':
            try:
                self.resp = requests.get(url=url, params=data)
            except AttributeError as e:
                mylog.error('http请求GET出错了！！{}'.format(e))
                raise e
        elif method.upper() == 'POST':
            try:
                self.resp = requests.post(url=url, data=data ,cookies = cookies)
            except AttributeError as e:
                mylog.error('http请求POST出错了！！{}'.format(e))
                raise e
        elif method.upper() == 'DELETE':
            try:
                self.resp = requests.delete(url=url, param=data)
            except AttributeError as e:
                mylog.error('http请求DELETE出错了！！{}'.format(e))
                raise e
        else:
            mylog.error('http请求没有{}这个方法'.format(method))

    def get_txt(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()

    def cookies(self):
        return  self.resp.cookies

    def status_code(self):
        return self.resp.status_code