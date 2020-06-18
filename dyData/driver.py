from common import *
from readConf import *
import random


if __name__ == "__main__":
    #从dy首页开始
    home = Element('dy_a70_home.xml')
    morehot = Element('dy_a70_morehot.xml')
    word_list = Element('dy_a70_word_list.xml')
    word_detail = Element('dy_a70_word_detail.xml')
    event = Event()

    # #找到搜索
    # search = element.findElementById('com.ss.android.ugc.aweme:id/amj')
    # event.touch(search[0],search[1])
    #
    # #查看更多热搜榜
    # lookup = element.findElementById('com.ss.android.ugc.aweme:id/b88')
    # event.touch(lookup[0],lookup[1])


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
    for i in range(len(hot)):
        x = hot[i][0]
        y = hot[i][1]
        event.touch(x,y)
        time.sleep(random.randint(1,9))
        #视频
        video = word_detail.findElementByName('视频')
        event.touch(video_tab_cord[0],video_tab_cord[1])
        time.sleep(round(random.uniform(0,9),2))
        event.touch(video_word_detail_back_cord[0],video_word_detail_back_cord[1])
        time.sleep(round(random.uniform(0,9),2))

    #回到查看更多热点
    event.touch(video_word_detail_back_cord[0],video_word_detail_back_cord[1])

    #回到首页。
    event.touch(video_word_detail_back_cord[0],video_word_detail_back_cord[1])


