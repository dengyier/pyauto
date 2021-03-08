'''
Create on:2020-12-10
@author: 麒麟
@email：denghaibo@sfmail.sf-express.com
模拟第三方API发起执行SQL请求
'''
from parameterized import  parameterized,param
import unittest
import hashlib
import time
import requests
import json
import random
import string
'''
6带扫描  0.待执行 1执行中 2已完成 3 已完成 4取消 5待优化'''
def execute_sql(url,appKey,appName,userID,userName,sql):
    queryId = int(round(time.time() * 1000))
    para = {}
    para['appName'] = appName
    para['timeStamp'] = int(round(time.time() * 1000))
    para['userId'] = userID
    para['userName'] = userName
    para['sql'] = sql
    para['queryId'] = queryId

    signdata = appKey + getSignData(para)
    para['singal'] = hashlib.sha1(signdata.encode("utf8")).hexdigest()

    print(hashlib.sha1(signdata.encode("utf8")).hexdigest())

    params = json.dumps(para)
    print(params)
    res = requests.post(url, data=params, headers={'Content-Type': 'application/json'})

    if res.status_code == 200:
        # print(res.status_code)
        print(res.content.decode())
        query_status(appName,queryId,appKey)
        return res.status_code
    else:
        # print(res.status_code)
        print(res.content.decode())
        query_status(appName,queryId,appKey)
        return res.status_code

def getSignData(data):
    content = ksort(data)
    result = ''

    for i in range(len(content)):
        if (i == 0):
            result = str(content[i][1])
        else:
            result += str(content[i][1])

    return result

def ksort(l):
    return [(k, l[k]) for k in sorted(l.keys())]

def query_status(appname,query_id,appkey):
    query_url = 'http://10.210.40.145:8282/api/sql/status'

    params = {}
    params['appName'] = appname
    params['queryId'] = query_id
    signdata = appkey + getSignData(params)
    print('当前拼接字段为：'+signdata)

    params['singal'] = hashlib.sha1(signdata.encode("utf8")).hexdigest()

    # params = json.dumps(params)
    a = requests.get(query_url, params=params, headers={'Content-Type': 'application/json'})

    if a.status_code == 200:
        time.sleep(0.25)
        print(a.content.decode())
    else:
        time.sleep(0.25)
        print(a.content.decode())

class AdhocTest(unittest.TestCase):
    URL="http://10.210.40.145:8282/api/sql/exec_sql"
    appKey = "123"
    appName = "datafactory"
    worknum = random.randint(10000000,99999999)
    name = ''.join(random.sample(string.ascii_letters, 8))
    SQL = "select * from binlog.da_binlog limit 10"
    '''
    执行1条第三方SQL
    '''
    @parameterized.expand([
        param(URL, appKey, appName, worknum, name , SQL, 200)
    ])
    def test_one_sql(self,urls,appkey,app_name,user_id,user_name,sql,code):
        self.assertEqual(execute_sql(urls,appkey,app_name,user_id,user_name,sql),code)

    '''
    执行5条第三方SQL
    '''
    @parameterized.expand([
        param(URL, appKey, appName, worknum, name , SQL, 200),
        param(URL, appKey, appName, worknum, name , SQL, 200),
        param(URL, appKey, appName, worknum, name , SQL, 200),
        param(URL, appKey, appName, worknum, name , SQL, 200),
        param(URL, appKey, appName, worknum, name , SQL, 200)
    ])
    def test_five_sql(self, urls, appkey, app_name, user_id, user_name, sql, code):
        self.assertEqual(execute_sql(urls, appkey, app_name, user_id, user_name, sql), code)

    '''
    执行10条第三方SQL
    '''
    @parameterized.expand([
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200)
    ])
    def test_ten_sql(self,urls,appkey,app_name,user_id,user_name,sql,code):
        self.assertEqual(execute_sql(urls,appkey,app_name,user_id,user_name,sql),code)

    '''
    占满公共队列和第三方队列
    '''
    @parameterized.expand([
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200)
    ])
    def test_fifth_sql(self,urls,appkey,app_name,user_id,user_name,sql,code):
        self.assertEqual(execute_sql(urls,appkey,app_name,user_id,user_name,sql),code)

    '''
    所属队列已满，公共队列已满
    '''
    @parameterized.expand([
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200),
        param(URL, appKey, appName, worknum, name, SQL, 200)
    ])
    def test_sixth_sql(self,urls,appkey,app_name,user_id,user_name,sql,code):
        self.assertEqual(execute_sql(urls,appkey,app_name,user_id,user_name,sql),code)
if __name__ == '__main__':
    unittest.main()



