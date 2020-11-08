#!-*-coding: utf-8 -*-
#!Time  : 2020/11/7 10:11
#!@Author : 张俊彬
import decimal

import pymysql
from common.readConfig import readConfig
from common.myLog import MyLog


class MySql:
    def __init__(self):
        self.mylog = MyLog('Sql查询')
        self.conf = readConfig()
        host = self.conf.getstr('mysql','host')
        user = self.conf.getstr('mysql','user')
        password = self.conf.getstr('mysql','pwd')
        port= self.conf.getint('mysql','port')
        cursorclass = pymysql.cursors.DictCursor
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port,cursorclass= cursorclass)


    def fet_one(self, sql):
        cursor = self.mysql.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchone()
            self.mylog.debug('sql语句：{}，数据查询结果：{}'.format(sql ,res))
            self.mysql.close()
        except Exception as e:
            self.mylog.error('数据库查询出错啦！！【error】:{}'.format(e))
            raise e
        return res

    def fet_all(self, sql):
        cursor = self.mysql.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            self.mylog.debug('sql语句：{}，数据查询结果：{}'.format(sql, res))
            self.mysql.close()
        except Exception as e:
            self.mylog.error('数据库查询出错啦！！【error】:{}'.format(e))
            raise e
        return res

if __name__ == '__main__':

    mysql = MySql()
    # sql = "SELECT *  from future.member WHERE MobilePhone = '13822221113'"
    sql = "SELECT *  from future.member WHERE MobilePhone = '13822221113'"
    res = mysql.fet_one(sql=sql)
    leaveAmount = res['LeaveAmount']
    print(leaveAmount)
    afteramount = leaveAmount + decimal.Decimal('-11')
    print(afteramount)