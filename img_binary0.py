# 针对1位无噪验证码的二值化处理
import cv2

def img_binary0(t):
    image=cv2.imread('./data/org_img/%s.jpg'%t) # 读入图片
    th1=cv2.Canny(image,70,100) # 按色差进行边缘提取
    cv2.imwrite("./data/bin_img/binary_%s.jpg"%t,th1)
    print("finish%s"%t)