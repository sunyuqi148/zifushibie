# 针对不定位粘连双字体有噪含干扰线验证码的干扰线去除
import cv2
import queue

class Dot: # 把点抽象为一个类
    x = 0
    y = 0
    tag = 0
    def set_pos(self,_x, _y,_tag):
        self.x = _x
        self.y = _y
        self.tag = _tag
        return Dot
q = queue.Queue() # 广搜队列
buf = queue.Queue() # 缓冲队列

def bfs(vis,img,x_s,y_s):# 从某个黑像素出发进行广度优先搜索，该广搜只向右、右上、右下三个方向进行，提取出一片黑色区域
    find_line=0
    while (not q.empty()):
        p = q.get()
        buf.put(p)# 将广搜得到的像素点放入缓冲区
        if(p.x>100): # 如果该黑色区域的横向长度超过100，则认为它是一条干扰线
            find_line=1
        if(p.tag!=1):
            if(p.y+1<y_s and img[p.y+1,p.x]==0 and vis[p.x][p.y+1]==0):
                tx=p.x
                ty=p.y+1
                up=Dot()
                up.set_pos(tx,ty,1)
                vis[tx][ty]=1
                q.put(up)
            if (p.y - 1 >=0 and img[p.y-1, p.x]==0 and vis[p.x][p.y-1]==0):
                tx = p.x
                ty = p.y - 1
                down = Dot()
                down.set_pos(tx, ty, 1)
                vis[tx][ty] = 1
                q.put(down)
        if(p.x+1<x_s and img[p.y,p.x+1]==0 and vis[p.x+1][p.y]!=2):
            tx=p.x+1
            ty=p.y
            right=Dot()
            right.set_pos(tx, ty, 0)
            vis[tx][ty] = 2
            q.put(right)
    return find_line

def ought_rem(img,x_s,y_s,x,y,scope,c):# 判断干扰线上的像素点(x,y)是否应该去除
    count=0
    j=y-scope
    while (j <= y + scope):# 如果该像素的上下相邻区域存在黑点，则将其涂黑，否则应去除
        if (j < 0 or j >= y_s):
            j = j + 1
            continue
        if (img[j, x] != 255):
            count = count + 1
        if (count >= c):
            return 0
        j=j+1
    return 1

def whiteBlur(img): # 确定的干扰线同时去除了一些不应去掉的黑像素，这里尝试恢复一些
    x_size = img.shape[0]
    y_size = img.shape[1]
    for y in range(y_size):# 去白噪点，如果一个白点周围没有白点，则将其染黑
        for x in range(x_size):
            if(img[x,y]==255):
                if(x-1>=0 and img[x-1,y]==255):
                    continue
                if (x + 1 <x_size and img[x +1, y] == 255):
                    continue
                if (y-1>=0 and img[x, y-1] == 255):
                    continue
                if (y+1<y_size and img[x, y+1] == 255):
                    continue
                img[x, y] = 0
    return

T = 1
while (T < 100):
    image = cv2.imread('./data/bin_img/binary_%s.jpg' % T, 0) # 读入灰度图片
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 233, 7)# 二值化
    x_size = image.shape[1]
    y_size = image.shape[0]
    clr=image.copy()
    visit = [[0 for y in range(y_size)] for x in range(x_size)]
    j = y_size - 1
    while (j >= 0): # 广搜去线
        for i in range(20):
            if (visit[i][j] == 0 and image[j, i] < 50):
                dot=Dot()
                dot.set_pos(i,j,0)
                visit[i][j] = 1
                q.put(dot)
                if(bfs(visit,image,x_size,y_size) == 1):# 寻找到了干扰线，将其去除
                    while(not buf.empty()):
                        blank=buf.get()
                        if(ought_rem(image,x_size,y_size,blank.x,blank.y,5,5)==1):
                            clr[blank.y,blank.x]=255
                    break
                else:
                    while (not buf.empty()):# 此次广搜未找到干扰线，清空缓冲区
                        buf.get()
        j = j - 1
    whiteBlur(clr)
    cv2.imwrite("./data/clr_img/clear_%s.jpg" % T, clr)
    T= T + 1
