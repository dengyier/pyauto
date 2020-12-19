# -*- coding: utf-8 -*- import sys, locale
'''
Create on:2020-10-10
@author: 麒麟
@email：dhb0113@163.com
工具使用：
1）在Charles的Map remote中将上报host与127.0.0.1绑定
2）执行代码
3)手机挂代理，代理IP为当前本地IP
'''

import json
from flask import Flask, request
from base64 import b64decode
from gzip import decompress

app = Flask(__name__)


def write(path, data):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data)
        f.write('=' * 30)
        f.write('\n')

#刷宝埋点解析
@app.route('/sa', methods=["POST"])
def shuabao_run():
    info = request.values.to_dict()
    data_list = info['data_list']
    data1 = b64decode(data_list)
    data2 = decompress(data1)
    data3 = data2.decode('utf-8')
    data4 = json.dumps(json.loads(data3), indent=4, sort_keys=False, ensure_ascii=False)
    write(r'../Downloads/工作/debug1.log', data4)
    return data4


@app.route('/sa.gif', methods=["GET"])
def get_json():
    info = request.values.to_dict()
    data_list = info['data']
    data1 = b64decode(data_list)
    return data1
#刷步埋点解析
@app.route('/sa.gif',methods=["POST"])

def post_json_shuabu():
    info = request.values.to_dict()
    data_list = info['data_list']
    data_sb = b64decode(data_list)
    data_sb2 = decompress(data_sb)
    data_sb3 = data_sb2.decode('utf-8')
    data_sb4 = json.dumps(json.loads(data_sb3), indent=4, sort_keys=False, ensure_ascii=False)
    write(r'../Downloads/工作/debug1.log', data_sb4)
    return data_sb4

#找茬埋点解析
def post_json_zhaocha():
    info = request.values.to_dict()
    data_list_zc = info['data']
    data_sb_zc = b64decode(data_list_zc)
    data_sb_zc2 = decompress(data_sb_zc)
    data_sb_zc3 = data_sb_zc2.decode('utf-8')
    data_sb_zc4 = json.dumps(json.loads(data_sb_zc3), indent=4, sort_keys=False, ensure_ascii=False)
    write(r'../Downloads/工作/debug1.log', data_sb_zc4)
    return data_sb_zc4


if __name__ == '__main__':
    print(__name__)
# 定义运行端口
    app.run(port=8106)
