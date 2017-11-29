import cv2
import numpy as np  
from matplotlib import pyplot as plt

t=1
while (t<100):
    image=cv2.imread('./data/org_img/%s.jpg'%t)
    th1=cv2.Canny(image,70,100)
    x_size = th1.shape[0]
    y_size = th1.shape[1]
    for y in range(y_size):
        for x in range(x_size):
            th1[x,y]=255-th1[x,y]
    # kernel = np.ones((2, 2), np.uint8)
    # th1=cv2.erode(th1,kernel)
    cv2.imwrite("./data/bin_img/binary_%s.gloabl.jpg"%t,th1)
    print("finish%s"%t)
    t=t+1