import time
import os
for i in range(25):
    dt = input("输入时间：")
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    print(timestamp)