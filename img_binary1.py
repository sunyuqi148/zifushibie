# 针对4位无粘连有噪验证码的二值化处理
import cv2

def binary(img): # 以150为阈值进行二值化
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

def img_binary1(x):
    GrayImage=cv2.imread('./data/org_img/%s.jpg'%x,0) # 读入灰度图片
    bi=binary(GrayImage)
    for j in range(GrayImage.shape[0]): # 调整图片（去噪），如果一个黑点周围没有黑点，则视为噪点
        for i in range(GrayImage.shape[1]):
            if (bi[j,i] == 0 and bi[j+1,i] != 0 and bi[j-1,i] != 0):
                bi[j,i] = 255
    cv2.imwrite("./data/bin_img/binary_%s.jpg"%x,bi)
    print("binary finish%s"%x)