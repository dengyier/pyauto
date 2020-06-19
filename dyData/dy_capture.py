# -*-coding:utf-8*-
import requests
import  driver
from requests.adapters import HTTPAdapter
import  time,json
import  os, random
from urllib import parse
import base64
import hmac
from hashlib import sha1
import  file_utils

HEADER_CONTENT_TYPE = 'Content-Type'
HEADER_HOST = 'Host'
HEADER_UA = 'User-Agent'
HEADER_COOKIE = 'Cookie'
HOST_COUNT = 10
CONNECTION_PER_HOST = 50
TIMEOUT = 30
zxgSession = requests.Session()
request_retry = HTTPAdapter(max_retries=3 , pool_connections=HOST_COUNT, pool_maxsize=CONNECTION_PER_HOST)
zxgSession.mount('https://',request_retry)
zxgSession.mount('http://',request_retry)
pro = {"https": "http://127.0.0.1:8888", "http": "http://127.0.0.1:8888"}
pwp_key = ['A692F2DA1DE62335B14F97871A936D10', 'C417FAD740D2A9C0F6A8D5EB8EC49442',
           'F47041EFDF9FEC161ACA9675FD3AF1D0','08ABD18A6127D0BF456A87FF78CC88EB',
           '4FCEBE7EE0520538DDC399C04C8E99D8',
           'C43BDBEF9D11222B3BDB2BB2E1C37F29','3923AF60B8B717A2A33435213F4E80CB',
           '83B17DB10134202DAC7C1782B7081311','311AAB2A43FBD97739C9EAD3C4728149',
           '311AAB2A43FBD97739C9EAD3C4728149','5D1E11EB37B5F82FA619CA2159D1A665',
           'BFEB5D2F637E8059EABB8715FA37F7F8','BFEB5D2F637E8059EABB8715FA37F7F8']
headers = {
    'Accept-Encoding': 'gzip',
    HEADER_UA: 'ttplayer(version name:2.8.1.178,version code:281178,ttplayer release was built by tiger at 2019-01-24 14:59:31 on origin/master branch, commit 9dc9282470dfb291d6fee8391bf39c7a96c42570)',
    'Icy-MetaData': '1',
    'Connection': 'Keep-Alive',
    'Vpwp-Key': 'BFEB5D2F637E8059EABB8715FA37F7F8',
    'Accept':'*/*',
    'Vpwp-Flag': '0',
    'Accept-Encoding': 'identity'
}


last_words_file = 'dy_data.pkl'
last_words_dict= dict()


def load_data():
    global  last_words_dict
    last_words_dict = file_utils.load_from_file_by_name(last_words_file)

def save_data():
    file_utils.save_to_file_by_name(last_words_dict, last_words_file)

def url_decode(text):
    return parse.unquote(text, 'utf-8')


def get_uploading_files(upload_dir):
    ret = list()
    for fpathe, dirs, fs in os.walk(upload_dir):
        for f in fs:
            full_path = os.path.join(fpathe, f)
            if f.startswith('.'):
                continue
            ret.append(dict(full_name=full_path, short_name = url_decode(f)))
    return ret

def get_file(file_path):
    f = open(file_path, 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    f.close()
    return htmlstr

def pare_url_param(url):
    result = parse.urlparse(url=url,allow_fragments=True)
    return parse.parse_qs(result.query)

def update_word_list():
    global  last_words_dict
    for item  in get_uploading_files('/Users/jumei/Downloads/dy_mir/aweme.snssdk.com/aweme/v1/hot/search/list'):
        file_name = item['full_name']
        try:
            word_json = json.loads(get_file(file_name))
        except :
            os.remove(file_name)
            continue
        for  item in word_json['data']['word_list']:
            if 'group_id' in item:
                if item['group_id'] not in last_words_dict:
                    last_words_dict[item['group_id']] = {'word': item['word'],'hot_value':item['hot_value']}
                else:
                    last_words_dict[item['group_id']]['word'] =  item['word']
                    last_words_dict[item['group_id']]['hot_value'] = item['hot_value']
        os.remove(file_name)

def get_item_by_keyword(word):
    for id, item in last_words_dict.items():
        if item['word'] == word:
            return item
    return None

def update_video_list():
    for item  in get_uploading_files('/Users/jumei/Downloads/dy_mir/aweme.snssdk.com/aweme/v1/search/item'):
        file_name = item['full_name']
        try:
            word_json = json.loads(get_file(file_name))
        except:
            os.remove(file_name)
            continue
        url = 'http://www.jumei.com/query' + item['short_name']
        params = pare_url_param(url)
        if 'keyword' not in params:
            print ('no word in', item['short_name'])
            os.remove(file_name)
            continue
        keyword_ = params['keyword'][0]
        keyword_entity = get_item_by_keyword(keyword_)
        # print ('keyword', keyword_, keyword_entity)
        if keyword_entity is None or 'aweme_list' not in word_json or word_json['aweme_list'] is None:
            os.remove(file_name)
            continue
        for item in word_json['aweme_list']:
            if 'video_dict' not in keyword_entity:
                keyword_entity['video_dict'] = dict()
            entity = get_url_from_videoinfo(item)
            if entity is None:
                continue
            keyword_entity['video_dict'][item['aweme_id']] = entity
            if 'hot_info' in item:
                keyword_entity['rank'] = item['hot_info']['rank']
        os.remove(file_name)


def get_url_from_videoinfo(item):
    bitrate = item['video']['bit_rate'][0]
    address = bitrate['play_addr']
    uri = address['url_key']
    url = address['url_list'][0]
    if 'author' not in item:
        return None
    author = item['author']
    return dict( uri=uri, url=url, username = author['nickname'], signature = author['signature']
                 ,desc = item['desc'])

def upload_tpdns():
    to_pop_word_ids = set()
    for word_id, item in last_words_dict.items():
        word = item['word']
        if 'video_dict' not in item or len(item['video_dict']) == 0:
            to_pop_word_ids.add(word_id)
            continue
        expired_video_ids = set()
        for video_id, video in item['video_dict'].items():
            url = video['url']
            uri = video['uri']
            # cmd = 'curl  -o ./%s.mp4  %s' %(uri, url)
            headers['Vpwp-Raw-Key'] = uri
            headers['Vpwp-Key'] = random.choice(pwp_key)
            local_file_name ="./%s.mp4" % uri
            save_local = False
            if save_local:
                if not os.path.exists(local_file_name):
                    suc , res = get_url_response(url)
                    if not suc:
                        expired_video_ids.add(video_id)
                        print ('not 200', url)
                        continue
                    else:
                        with open(local_file_name, "wb") as f:
                            for chunk in res.iter_content(chunk_size=512):
                                f.write(chunk)
                        print (url)
            else :
                if 'jmcdn_url' not in video:
                    suc , res = get_url_response(url)
                    if not suc:
                        expired_video_ids.add(video_id)
                        print ('not 200', url)
                        continue
                    else:
                        jmcdn = change_video_url(res.content, str(res.headers['Content-Length']))
                        if jmcdn['code'] == 1000:
                            video['jmcdn_url'] = jmcdn['url']
                            print (jmcdn['url'])

        for vid in expired_video_ids:
            item['video_dict'].pop(vid)
    for id in to_pop_word_ids:#删除没有视频的话题
        last_words_dict.pop(id)

def get_url_response(url ):
    try:
        res = zxgSession.get(url, headers= headers, proxies = pro, timeout = TIMEOUT)
        if int(res.status_code) != 200 or 'video/mp4' not in res.headers['Content-Type']:
            return False , res
        return True, res
    except :
        return False , None

def change_video_url(file_content, file_length):
    server ='http://upload.jmvideo.jumei.com/app_upload'
    try:
        data = dict(user='160610490', extension='mp4',
                    content_range="bytes 0-%s/%s" %(file_length, file_length),
                    time=int(time.time()*1000))
        json_data = json.dumps(data)
        headers['token'] = get_upload_token(json_data)
        result = zxgSession.post(server, data=file_content, proxies = pro,headers=headers).text
        return json.loads(result)
    except Exception as e :
        print ('upload_jmcdn error', e)
        return dict(code = -1, url = '')

def url_safebase64(url):
    return base64.urlsafe_b64encode(url.encode("utf-8")).decode('utf-8')

def hash_hmac(code, key, sha1):
    hmac_code = hmac.new(key.encode("utf-8"), code.encode("utf-8"), sha1).digest()
    return base64.urlsafe_b64encode(hmac_code).decode('utf-8')

def upload_jmcdn(file_name):
    server ='http://upload.jmvideo.jumei.com/app_upload'
    try:
        data = dict(user='160610490', extension='mp4',
                    content_range=get_file_content_range(file_name),
                    time=int(time.time()*1000))
        json_data = json.dumps(data)
        headers['token'] = get_upload_token(json_data)
        result = zxgSession.post(server, data=open(file_name, 'rb'), proxies = pro,headers=headers).text
        return result
    except Exception as e :
        print ('upload_jmcdn error', e)
        return None

def get_file_content_range(file_name):
    len = os.path.getsize(file_name)
    return "bytes 0-%d/%d" %(len, len)

def get_upload_token(text):
    safebase_ = url_safebase64(text)
    return '%s:%s' %(hash_hmac(safebase_, "Wy5gZ1y$0%$bsrE6MbNq1OI3mdevxdQx", sha1), safebase_)

def write_content(text):
    with open("./out.json","w") as f:
        f.write(text)


if __name__ == "__main__":
    print('start run')
    driver.start_run_from_homepage()
    load_data()
    update_word_list()
    update_video_list()
    print('start upload')
    upload_tpdns()
    save_data()
    write_content(json.dumps(last_words_dict))


