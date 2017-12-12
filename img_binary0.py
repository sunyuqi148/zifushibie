import cv2
import numpy as np  
from matplotlib import pyplot as plt

# def img_binary0(t):
t=0
while(t<100):
    image=cv2.imread('./data/org_img/%s.jpg'%t)
    th1=cv2.Canny(image,70,100) # 按色差进行边缘提取
    x_size = th1.shape[0]
    y_size = th1.shape[1]
    cv2.imwrite("./data/bin_img/binary_%s.jpg"%t,th1)
    print("finish%s"%t)
    t=t+1