import cv2
import numpy as np  
from matplotlib import pyplot as plt

def blackBlur(img, scope, c):
    x_size=img.shape[0]
    y_size=img.shape[1]
    re = img
    for y in range(y_size):
        for x in range(x_size):
            if(re[x,y]==255):
                continue
            count=0
            i = x - scope
            while (i<=x+scope):
                if (i < 0 or i >= x_size):
                    i=i+1
                    continue
                j = y - scope
                while (j<=y+scope):
                    if(j<0 or j>=y_size):
                        j=j+1
                        continue
                    if(img[i,j]==0):
                        count=count+1
                    j = j + 1
                if (count >= c):
                    break
                i = i + 1
            if(count<c):
                re[x,y]=255
    return re

def whiteBlur(img, scope, c):
    x_size=img.shape[0]
    y_size=img.shape[1]
    re = img
    for y in range(y_size):
        for x in range(x_size):
            if(re[x,y]==0):
                continue
            count=0
            i = x - scope
            while (i<=x+scope):
                j = y - scope
                while (j<=y+scope):
                    if(i<0 or i>=x_size or j<0 or j>=y_size or img[i,j]==255):
                        count=count+1
                    j = j + 1
                if (count > c):
                    break
                i = i + 1
            if(count<=c):
                re[x,y]=0
    return re

x=1
while (x<50):
    GrayImage=cv2.imread('./data/org_img/%s.jpg'%x,0)
    th1 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,233,7)
    GrayImage= cv2.medianBlur(th1,3)
    for j in range(GrayImage.shape[1]):
        for i in range(GrayImage.shape[0]):
            if (th1[i,j] == 0):
                th1[i,j] = GrayImage[i,j]
    th1=blackBlur(th1, 2, 7)
    # th1 = whiteBlur(th1, 1, 2) 未完善
    cv2.imwrite("./data/bin_img/binary_%s.gloabl.jpg"%x,th1)
    print("finish%s"%x)
    x=x+1