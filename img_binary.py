import cv2
import numpy as np  
from matplotlib import pyplot as plt  
GrayImage=cv2.imread('./data/org_img/1.jpg',0)  
ret, th1 = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)  
GrayImage= cv2.medianBlur(GrayImage,5)  
th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)  
th3 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
cv2.imwrite("./data/bin_img/binary_1.gloabl.jpg",th1)
cv2.imwrite("./data/bin_img/binary_1.adaptive.mean.jpg",th2)
cv2.imwrite("./data/bin_img/binary_1.adaptive.gaussian.jpg",th3)