from dyData.common import *
from readConf import *
import random


if __name__ == "__main__":
    element = Element()
    event = Event()

    # #找到搜索
    # search = element.findElementById('com.ss.android.ugc.aweme:id/amj')
    # event.touch(search[0],search[1])
    #
    # #查看更多热搜榜
    # lookup = element.findElementById('com.ss.android.ugc.aweme:id/b88')
    # event.touch(lookup[0],lookup[1])

    #查看热搜榜
    hot = element.findElementsByClass('android.widget.RelativeLayout')
    for i in range(len(hot)):
        x = hot[i][0]
        y = hot[i][1]
        event.touch(x,y)
        time.sleep(random.randint(1,9))
        #视频
        video = element.findElementByName('视频')
        # event.touch(video[0],video[1])
        event.touch(355,264)
        time.sleep(round(random.uniform(0,9),2))
        event.touch(82,134)

