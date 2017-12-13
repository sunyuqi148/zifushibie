# 针对4位无粘连验证码的分割
from PIL import Image, ImageDraw
import queue
q = queue.Queue() # 广搜队列
buf = queue.Queue() # 缓冲队列

def bfs(vis,img,n): # 从某个黑像素出发进行广度优先搜索，提取出一个符号
    x_size, y_size = img.size
    l=x_size-1
    r=0
    while (not q.empty()):
        p = q.get()
        if(l>p[0]):
            l=p[0]
        if(r<p[0]):
            r=p[0]
        buf.put(p) # 将广搜得到的像素点放入缓冲区，等待切割
        left=(p[0]-1,p[1])
        right=(p[0]+1,p[1])
        up = (p[0], p[1]-1)
        down = (p[0], p[1]+1)
        if(left[0]>=0 and vis[left[0]][left[1]]==0 and img.getpixel(left)<50):
            q.put(left)
            vis[left[0]][left[1]] =1
        if (right[0] < x_size and vis[right[0]][right[1]] == 0 and img.getpixel(right)<50):
            q.put(right)
            vis[right[0]][right[1]] = 1
        if (up[1] >= 0 and vis[up[0]][up[1]] == 0 and img.getpixel(up)<50):
            q.put(up)
            vis[up[0]][up[1]] = 1
        if (down[1] < y_size and vis[down[0]][down[1]] == 0 and img.getpixel(down)<50):
            q.put(down)
            vis[down[0]][down[1]] = 1
    return (l,r) # 返回该符号在图片中的左右边界值

def cut(x_size,y_size,n,part_n,offset): # 对第part_n部分进行切割，长和高分别为x_size和y_size
    out = Image.new('L', (x_size, y_size), 255) # 创建新图片
    draw = ImageDraw.Draw(out)
    while(not buf.empty()): # 将buf中的像素填充至新图片
        p=buf.get()
        change=(p[0]-offset,p[1])
        draw.point(change, fill = 0)
    out.save("./data/part/%s-"%n+str(part_n)+".jpg")
    return


def cut1(x):
    image = Image.open("./data/bin_img/binary_%s.jpg"%x)
    n=1 # 切割的图片部分编号
    x_size, y_size = image.size
    visit = [[0 for y in range(y_size)] for x in range(x_size)]
    for j in range(y_size): # 寻找一个黑像素，进行广搜，搜完之后立即切割
        for i in range(x_size):
            if (visit[i][j] == 0 and image.getpixel((i,j)) <50):
                visit[i][j] = 1
                q.put((i,j))
                width=bfs(visit,image,n)
                cut(width[1]-width[0]+1,y_size,x,n,width[0])
                n=n+1