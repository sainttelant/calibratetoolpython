import cv2
import sys
import time
import datetime
import os

if __name__ == "__main__":
    radar_no = str(sys.argv[1])
    radar_camera = {'81': ['11.89.197.8', 'admin', 'qianfang123'],
                    '82': ['11.89.197.2', 'admin', 'qianfang123'],
                    '83': ['11.89.197.6', 'admin', 'qianfang123'],
                    '84': ['11.89.197.4', 'admin', 'qianfang123'],
                    '215': ['10.203.204.198', 'admin', 'Ucit2021']}
    if not radar_camera.get(radar_no):
        print('ERROR radar number: %s' % radar_no)
        exit(-1)
    
    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d")
    print(currentdate)
    abspath = os.getcwd()
    	
    if not os.path.exists(abspath+"/ecals/%s/"%(currentdate)):
        os.makedirs(abspath+"/ecals/%s/"%(currentdate))
        print("create folder for video recording!")
    recordpath = abspath+"/ecals/%s/"%(currentdate)

    address, user, pwd = radar_camera[radar_no]
    # 子码流
    #video_src = 'rtsp://%s:%s@%s:554/ch1/sub/av_stream' % (user, pwd, address)

    #主码流
    video_src = "rtsp://%s:%s@%s:554/h264/ch1/main/av_stream" % (user, pwd, address)
    print(video_src)
    cap = cv2.VideoCapture(video_src)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(frame_height,frame_width)
    fps = cap.get(cv2.CAP_PROP_FPS) #视频平均帧率
    print(fps)
    timestart = cv2.getTickCount()
    while cap.isOpened():
        ret, frm = cap.read()
        #print(frm.shape)
        #cv2.namedWindow('camera-215', 0)
        cv2.imshow('camera-215', frm)
        timestamp = int(time.time()*1000)
        #print(timestamp)
        cv2.imwrite(recordpath+str(timestamp)+".jpg",frm)
        timenow = cv2.getTickCount()
        duration = (timenow-timestart)/cv2.getTickFrequency()
        print("duration:",duration)
        key = cv2.waitKey(1)
        if key == 27 or (duration>30):
            os._exit(0)



