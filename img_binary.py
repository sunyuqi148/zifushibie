import cv2  
import os
import numpy as np  
from matplotlib import pyplot as plt  

img=cv2.imread('.\\data\\1.jpg',0)  
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)    
cv2.imwrite("1.jpg", thresh1)