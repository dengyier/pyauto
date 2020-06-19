from common import *
from readConf import *
import random


def start_run_from_homepage():
    #从dy首页开始
    home = Element('dy_a70_home.xml')
    morehot = Element('dy_a70_morehot.xml')
    word_list = Element('dy_a70_word_list.xml')
    word_detail = Element('dy_a70_word_detail.xml')
    event = Event()
    search_cord = home.findElementById('com.ss.android.ugc.aweme:id/amj')
    event.touch(search_cord[0], search_cord[1])#点击搜索
    time.sleep(round(random.uniform(0,9),2))

    morehot_cord = morehot.findElementById('com.ss.android.ugc.aweme:id/b88')
    event.touch(morehot_cord[0], morehot_cord[1])#点击查看更多热点
    time.sleep(round(random.uniform(0,9),2))

    video_tab_cord = word_detail.findElementByName('视频')
    video_word_detail_back_cord = word_detail.findElementById('com.ss.android.ugc.aweme:id/adb')
    print(search_cord, morehot_cord, video_tab_cord, video_word_detail_back_cord)
    #查看热搜榜
    hot = word_list.findElementsById('com.ss.android.ugc.aweme:id/b8f')


if __name__ == "__main__":
    start_run_from_homepage()

