import pymysql
import json
import requests
def get_sql(test_sql):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='zentao', charset='utf8')
    cur = conn.cursor()
    cur.execute(test_sql)
    data = cur.fetchall()
    #count = [d[0] for d in data ]
    #assignto = [d[1] for d in data ]
    return list(data)
    #cur.close()
    #conn.close()

def exec_post():
    sql = "SELECT  count(t1.id),t1.assignedTo,t2.realname,t1.id FROM zt_bug t1 INNER JOIN zt_user t2 ON t1.assignedTo=t2.account WHERE t1.STATUS='active' AND t1.assignedTo !='closed' GROUP BY t1.assignedTo"
    a = get_sql(sql)
    print(a)
    url = 'http://10.210.36.3:9603/api/message'
    for i in a:
        param = {}
        param['group_id'] = 5
        param['users']  = i[1]
        param['message'] = '尊敬的'+' '+i[2]+' '+'您好，您当前剩余BUG数：'+str(i[0])+' '+'详情请查看：'+' '+'http://10.210.40.51/zentao/bug-view-'+str(i[3])+'.html'

        params = json.dumps(param)
        print(params)
        res = requests.post(url, data=params, headers={'Content-Type': 'application/json'})
        if res.status_code ==200:
            print(res.content.decode())
        else:
            print(res.content.decode())
if __name__ == '__main__':
    exec_post()