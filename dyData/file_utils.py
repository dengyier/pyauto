# -*-coding:utf-8*-

import pickle
import  os

def save_to_file_by_name(dat, fileName):
    dir_name = '.%sdb%s'%(os.path.sep, os.path.sep)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    mydb  = open('.%sdb%s%s'%(os.path.sep, os.path.sep, fileName), 'wb')
    pickle.dump(dat, mydb, -1)
    mydb.close()

def load_from_file_by_name(fileName):
    path = '.%sdb%s%s'%(os.path.sep, os.path.sep, fileName)
    if not os.path.exists(path):
        # print(u'%s does not exist' % path)
        return dict()
    try:
        mydb = open(path, 'rb')
        table = pickle.load(mydb)
        mydb.close()
        return table
    except:
        # print(u'load %s failed' % path)
        return  dict()