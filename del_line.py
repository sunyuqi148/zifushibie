import cv2
import numpy as np
import queue


class Dot:
    x = 0
    y = 0
    tag = 0

    def set_pos(self,_x, _y,_tag):
        self.x = _x
        self.y = _y
        self.tag = _tag
        return Dot


q = queue.Queue()
buf = queue.Queue()

def bfs(vis,img,x_s,y_s):
    find_line=0
    while (not q.empty()):
        p = q.get()
        px=p.x
        py=p.y
        buf.put(p)
        if(p.x>100):
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

def ought_rem(img,x_s,y_s,x,y,scope,c):
    count=0
    j=y-scope
    while (j <= y + scope):
        if (j < 0 or j >= y_s):
            j = j + 1
            continue
        if (img[j, x] != 255):
            count = count + 1
        if (count >= c):
            return 0
        j=j+1
    return 1

x = 1
while (x < 50):
    image = cv2.imread('./data/bin_img/binary_%s.gloabl.jpg' % x, 0)
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 233, 7)
    x_size = image.shape[1]
    y_size = image.shape[0]
    visit = [[0 for y in range(y_size)] for x in range(x_size)]
    j = y_size - 1
    while (j >= 0):
        for i in range(20):
            if (visit[i][j] == 0 and image[j, i] < 50):
                dot=Dot()
                dot.set_pos(i,j,0)
                visit[i][j] = 1
                q.put(dot)
                if(bfs(visit,image,x_size,y_size) == 1):
                    while(not buf.empty()):
                        blank=buf.get()
                        if(ought_rem(image,x_size,y_size,blank.x,blank.y,5,6)==1):
                           image[blank.y,blank.x]=255
                    break
                else:
                    while (not buf.empty()):
                        buf.get()
        j = j - 1
    cv2.imwrite("./data/clr_img/clear_%s.jpg" % x, image)
    print("finish%s" % x)
    x= x + 1
