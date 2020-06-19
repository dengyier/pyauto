import unittest
from common.readMysql import MySql
from config.readConfig import *

if __name__ == '__main__':
    cn = MySql(host=host,user=user,passwd=passwd,db=db_name)
    cn.exec_data()
    cn.conn_db()
    cn.select('select * from test ')

