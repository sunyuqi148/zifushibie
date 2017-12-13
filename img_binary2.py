# 针对4位有噪含干扰线验证码的二值化处理
import cv2
import os
import queue
buf1 = queue.Queue() # 缓冲队列1
buf2 = queue.Queue() # 缓冲队列2

def find_line(img): # 利用干扰线的颜色比其他地方深，标出干扰线，并把干扰线放入缓冲队列1
    x_size=img.shape[0]
    y_size=img.shape[1]
    re = img.copy()
    for y in range(y_size):
        for x in range(x_size):
            if(re[x,y][0]<23 and re[x,y][1]<23 and re[x,y][2]<23):
                buf1.put((x,y))
    return re

def ought_rem(img,x_s,y_s,x,y,scope,c): # 判断干扰线上的像素点(x,y)是否应该去除
    count=0
    j=y-scope
    while (j <= y + scope): # 如果该像素的上下相邻区域存在黑点，则将其涂黑，否则应去除
        if (j < 0 or j >= y_s):
            j = j + 1
            continue
        if (img[j, x] ==0):
            count = count + 1
        if (count >= c):
            return 1
        j=j+1
    return 0

def binary(img): # 以150为阈值进行二值化，并处理干扰线
    x_size=img.shape[0]
    y_size=img.shape[1]
    re = img.copy()
    for y in range(y_size):
        for x in range(x_size):
            if(re[x,y]>150):
                re[x,y]=255
            else:
                re[x,y]=0
    while (not buf1.empty()): # 将干扰线从buf1中取出并暂时标记为灰色，放入buf2中等待判断
        t = buf1.get()
        re[t[0], t[1]] = 200
        buf2.put(t)
    while(not buf2.empty()): # 处理干扰线，一些部分（字符的躯干）部分应为黑色，其他地方为白色
        t = buf2.get()
        if (ought_rem(re, y_size, x_size, t[1], t[0], 5, 5) == 1):
            re[t[0],t[1]] = 0
        else:
            re[t[0], t[1]] = 255
    return re



def img_binary2(x):
    Image=cv2.imread('./data/org_img/%s.jpg'%x) # 读入图片
    bi=find_line(Image) # 标出干扰线
    cv2.imwrite("./data/bin_img/temp.jpg", bi)
    Image = cv2.imread("./data/bin_img/temp.jpg",0)  # 重新读入灰度图片
    bi = binary(Image) # 图片二值化
    x_size = Image.shape[1]
    y_size = Image.shape[0]
    for j in range(Image.shape[0]): # 图片四周边框设为白色
        bi[j,0]=bi[j,x_size-1]=255
    for i in range(Image.shape[1]):
        bi[0,i] = bi[y_size-1,i] = 255
    j=1
    while(j<y_size-1): # 进行两次全局去噪点，如果一个黑点周围没有黑点，则视为噪点
        i=1
        while(i<x_size-1):
            if ((bi[j,i] == 0 and bi[j+1,i] != 0 and bi[j-1,i] != 0)
                or (bi[j, i] == 0 and bi[j, i+1] != 0 and bi[j, i-1] != 0)):
                bi[j,i] = 255
            i=i+1
        j=j+1
    j = 1
    while (j < y_size - 1):
        i = 1
        while (i < x_size - 1):
            if ((bi[j, i] == 255 and bi[j + 1, i] != 255 and bi[j - 1, i] != 255)
                or (bi[j, i] == 255 and bi[j, i + 1] != 255 and bi[j, i - 1] != 255)):
                bi[j, i] = 0
            i = i + 1
        j = j + 1
    cv2.imwrite("./data/bin_img/binary_%s.jpg"%x,bi)
    os.remove("./data/bin_img/temp.jpg") # 删除生成的临时文件