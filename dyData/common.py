import os
import time
import re
import xml.etree.cElementTree as ET
from dyData.readConf import *


class Element(object):
    def __init__(self):
        """
        初始化，获取文件存放目录
        """
        # self.Path = os.path.join(os.getcwd(),'dyData')
        self.Path = '/Users/yaoyao/Learn/dyData/'
        self.pattern = re.compile(r"\d+")
    def __uidump(self):
        """获取当前Activity控件树"""
        os.popen(cmdUi)
        os.popen(cmdPull+' ' + self.Path)
    def __element(self, attrib, name):
        '''同属性单个元素，返回单个元素坐标'''
        #self.__uidump()
        tree = ET.ElementTree(file= self.Path+'/ui.xml')
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                return Xpoint,Ypoint

    def __elements(self, attrib, name):
        """
        同属性多个元素，返回坐标元组列表
        """
        list = []
        #self.__uidump()
        tree = ET.ElementTree(file=self.Path + "/ui.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                list.append((Xpoint, Ypoint))
        return list

    def findElementByName(self, name):
        '''通过定位name元素'''
        return self.__element("text", name)

    def findElmentsByName(self, name):
        return self.__elements("text", name)

    def findElementByClass(self, className):
        return self.__element("class",className)

    def findElementsByClass(self, className):
        return self.__elements("class",className)

    def findElementById(self, id):
        return self.__element("resource-id",id)

    def findElementsById(self, id):
        return self.__elements("resource-id",id)

class Event(object):
    def __init__(self):
        os.popen(cmdWait)
    def touch(self,dx,dy):
        os.popen(cmdTap+" "+str(dx)+" "+str(dy))
        time.sleep(1)


def test():
    element = Element()
    event = Event()
    search = element.findElementById('com.ss.android.ugc.aweme:id/amj')
    event.touch(search[0],search[1])










