'''
Create on:2020-01-18
@author: 麒麟
@email：haibod@jumei.com
    pymysql是python3中用于MySQL数据库连接的模板，readMysql.py主要用于封装MySQL数据库的连接、执行SQL方法、查询、关闭
'''

import pymysql

class MySql(object):
    #初始化方法
    def __init__(self,host,user,passwd,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
    #封装一个连接数据库方法
    def conn_db(self):
        try:
            #使用pymysql.connect实例化一个对象
            self.conn = pymysql.connect(host = self.host,user = self.user,password = self.passwd,db = self.db,charset ='utf-8')
            self.conn.ping(True)
            self.cursor = self.conn.cursor()
        except Exception as e:
            self.conn = None
            self.cursor = None
            print(e.message)
    #封装一个执行SQL方法
    def exec_data(self,sql,data=None):
        try:
            self.conn_db()
            self.cursor.execute(sql,data)
            self.db.commit()
            self.close_conn()
        except Exception as e:
            print(e.message)
    #封装一个查询方法
    def select(self,sql):
        try:
            self.conn_db()
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                print(row)
            self.close_conn()
            return results
        except Exception as e:
            print(e.message)
    #封装关闭连接方法
    def close_conn(self):
        self.cursor.close()
        self.db.close()







