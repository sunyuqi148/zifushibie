import cv2
import numpy as np  
from matplotlib import pyplot as plt

def etract(img, scope, c):
    x_size=img.shape[0]
    y_size=img.shape[1]
    re = img.copy()
    for y in range(y_size):
        for x in range(x_size):
            if(re[x,y]>150):
                re[x,y]=255
            else:
                re[x,y]=0
    return re

x=1
while (x<100):
    GrayImage=cv2.imread('./data/org_img/%s.jpg'%x,0)
    # th1 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,233,7)
    # GrayImage= cv2.medianBlur(th1,3)
    # for j in range(GrayImage.shape[1]):
    #     for i in range(GrayImage.shape[0]):
    #         if (th1[i,j] == 0):
    #             th1[i,j] = GrayImage[i,j]
    th1=etract(GrayImage, 2, 7)
    cv2.imwrite("./data/bin_img/binary_%s.gloabl.jpg"%x,th1)
    print("finish%s"%x)
    x=x+1