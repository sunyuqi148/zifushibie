# 针对不定位粘连双字体有噪含干扰线验证码的二值化处理
import cv2

def blackBlur(img, scope, c): # 去除黑噪点，观察某黑点周围scope范围的环境，如果白点超过一定数量c，则去除
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

x=1
while (x<100):
    GrayImage=cv2.imread('./data/org_img/%s.jpg'%x,0) # 读入灰度图片
    th1 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,233,7) # 二值化
    GrayImage= cv2.medianBlur(th1,3) # 去噪
    for j in range(GrayImage.shape[1]):
        for i in range(GrayImage.shape[0]):
            if (th1[i,j] == 0):
                th1[i,j] = GrayImage[i,j]
    th1=blackBlur(th1, 2, 7) # 调整（更好地去除黑噪点）
    cv2.imwrite("./data/bin_img/binary_%s.jpg"%x,th1)
    x=x+1