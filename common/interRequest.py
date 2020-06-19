import requests
import json
class Apprequest:
    def get(self,url,para,headers):
        try:
            r = requests.get(url,params=para,headers=headers)
            print("获得返回状态码 ",r.status_code)
            json = r.json()
            print("json类型转换成python数据类型",json)
        except BaseException as e:
            print("请求失败",e.__context__)

    def post(self,url,para,headers):
        try:
            r = requests.post(url,params=para,headers=headers)
            print("获得返回状态码 ", r.status_code)
            json = r.json()
            print("json类型转换成python数据类型", json)

        except BaseException as e:
            print("请求失败", e.__context__)

    def post_json(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)
            r = requests.post(url,data=data,headers=headers)
            print("获得返回状态码 ", r.status_code)
            json_r = r.json()
            print("json类型转换成python数据类型", json_r)
        except BaseException as e:
            print("请求失败",e.__context__)



