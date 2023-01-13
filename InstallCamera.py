#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
import cv2 
import numpy as np
import math
import sys
ip = input("请输入相机的IP地址，格式为10.203.204.198")

cap = cv2.VideoCapture("rtsp://admin:Ucit2021@{}:554//Streaming/Channels/1".format(ip))
if False == cap.isOpened():
    
    print ("打开相机失败，查看输入IP是否正确")
    sys.exit()
else:
    print("相机打开，输入IP正确")
choose =[]
points = []
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        coord = ()
        coord = (x,y)
        
        calc = [x,y]
        cv2.circle(orignew, coord, 5, (255, 0, 0), thickness=-1)
        cv2.putText(orignew, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    2.0, (255, 255, 255), thickness=2)
        choose.append(coord)
        points.append(calc)
        cv2.imshow("orig",orignew)
        
def cal_area(vertices): #Gauss's area formula 高斯面积计算
    A = 0.0
    point_p = vertices[-1]
    for point in vertices:
        A += (point[1]*point_p[0] - point[0]*point_p[1])
        point_p = point
    return abs(A)/2

def cal_centroid(points):
    A = cal_area(points)
    c_x, c_y = 0.0, 0.0
    point_p = points[-1] # point_p 表示前一节点
    for point in points:
        c_x +=((point[0] + point_p[0]) * (point[1]*point_p[0] - point_p[1]*point[0]))
        c_y +=((point[1] + point_p[1]) * (point[1]*point_p[0] - point_p[1]*point[0]))
        point_p = point

    return c_x / (6*A), c_y / (6*A)



next = 0     
print(">>>>>>>>>>>>>>>>一定要顺时针取点，不支持交叉取点，和逆时针取点<<<<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>>一定要顺时针取点，不支持交叉取点，和逆时针取点<<<<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>>一定要顺时针取点，不支持交叉取点，和逆时针取点<<<<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>>一定要顺时针取点，不支持交叉取点，和逆时针取点<<<<<<<<<<<<<<<<<<<")
ret,orig = cap.read()
cv2.namedWindow('orig', 1)
factor =2
print(orig.shape)
dim = (int(orig.shape[1]/factor), int(orig.shape[0]/factor))
print(dim)

orignew = cv2.resize(orig,dim, interpolation =cv2.INTER_AREA)
cv2.setMouseCallback("orig", on_EVENT_LBUTTONDOWN)

cv2.imshow("orig",orignew)
cv2.waitKey(0)
cv2.destroyWindow("orig")

nums = len(choose)
print("choose the boundary points are:",points)

point = np.array(points)
centerx,centery = cal_centroid(point)


print("center point is({},{})".format(int(centerx),int(centery)))

cx = int(centerx)
cy = int(centery)

dist = math.sqrt(pow(cx-1280/factor,2)+pow(cy-720/factor,2))
print('dist',dist)

if dist < 20:
    print("installing appropriately, Okay!!!!")
    color = (255,0,0)
else:
    print("installing not well, Reinstalling!")
    color = (0,0,255)


if(nums<3):
    print("chosse points are less than 3, can't not comprise an area,quit!")
    next = 0
else:
    next =1
while next:
    ret,frame = cap.read()
    if True == cap.isOpened(): 
        ptop =(int(1280/factor),int(100/factor))
        pbottom=(int(1280/factor),int(1340/factor))
        pleft = (int(100/factor),int(720/factor))
        pright = (int(2460/factor),int(720/factor))
        #cv2.line()
        point_color = (0, 255, 0)  # BGR
        thickness = 5
        lineType = 4
        frame = cv2.resize(frame,dim, interpolation =cv2.INTER_AREA)
        for i in range(len(choose)-1):
            cv2.line(frame, choose[i], choose[i+1], (255,0,0), thickness, lineType)
        
        cv2.line(frame, choose[0], choose[nums-1], (255,0,0), thickness, lineType)    
        cv2.line(frame, ptop, pbottom, point_color, thickness, lineType)
        cv2.line(frame, pleft, pright, point_color, thickness, lineType)
        cv2.circle(frame, (int(1280/factor), int(720/factor)), int(40/factor), color, thickness=5)
        cv2.circle(frame,(int(centerx),int(centery)),10,(255,0,0),thickness=-1)
    
        cv2.line(frame, (int(1280/factor), int(720/factor)), (int(centerx),int(centery)), (0,0,255), 1, 4)
        cv2.namedWindow('frame', 1)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
cap.release()




# In[ ]:




