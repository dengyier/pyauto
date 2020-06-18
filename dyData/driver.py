from common import *
from readConf import *
import random


if __name__ == "__main__":
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
    morehot_cord = morehot.findElementById('com.ss.android.ugc.aweme:id/b88')

    print(search_cord, morehot_cord)
    #查看热搜榜
    hot = word_list.findElementsById('com.ss.android.ugc.aweme:id/b8f')
    print(len(hot),hot)
    for i in range(len(hot)):
        x = hot[i][0]
        y = hot[i][1]
        event.touch(x,y)
        time.sleep(random.randint(1,9))
        #视频
        video = word_detail.findElementByName('视频')
        # event.touch(video[0],video[1])
        event.touch(355,264)
        time.sleep(round(random.uniform(0,9),2))
        event.touch(82,134)
        time.sleep(random.randint(2,7))

