#import ecal.core.core as ecal_core
#from ecal.core.subscriber import StringSubscriber

import subprocess
import time
import datetime
import os
import sys

from threading import Thread
command_key = '' # 此键用来控制图片播放、停止以及程序退出

# 定义一个实时获取键盘输入的程序
def get_command(): 
    global command_key # 因为后续要对这个command_key 进行修改，所以这里需要声明成global
    command_key = input() # 获取输入
    get_command() # 获取下一次输入


def recordecal(a,b):
    print(a)
    subprocess.call(["ecal_rec","-r","30","-n","ecal_mea","--whitelist","ARS4G0_ObjectListPb215","-d",b])
    print("<<<<<<<<<<<<finished!")
    os._exit(0)
if __name__ == "__main__":
    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d")
    abspath = os.getcwd()	
    if not os.path.exists(abspath+"/ecals/%s/"%(currentdate)):
        os.makedirs(abspath+"/ecals/%s/"%(currentdate))
        print("create folder for video recording!")

    thd = Thread(target = get_command) #线程定义
    thd.start() # 开启线程
    recordpath = abspath+"/ecals/%s/"%(currentdate)
    recordecal("begin to record ecal datas",recordpath)
