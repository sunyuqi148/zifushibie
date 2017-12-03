from PIL import Image, ImageDraw
import queue
q = queue.Queue()
buf = queue.Queue()

def bfs(vis,img,n):
    x_size, y_size = img.size
    l=x_size-1
    r=0
    while (not q.empty()):
        p = q.get()
        if(l>p[0]):
            l=p[0]
        if(r<p[0]):
            r=p[0]
        buf.put(p)
        left=(p[0]-1,p[1])
        right=(p[0]+1,p[1])
        up = (p[0], p[1]-1)
        down = (p[0], p[1]+1)
        test1=img.getpixel(left)
        test2 = img.getpixel(right)
        test3= img.getpixel(up)
        test4 = img.getpixel(down)
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
    return (l,r)

def cut(x_size,y_size,n,part_n,offset):
    out = Image.new('L', (x_size, y_size), 255)
    draw = ImageDraw.Draw(out)
    while(not buf.empty()):
        p=buf.get()
        change=(p[0]-offset,p[1])
        draw.point(change, fill = 0)
    out.save("./data/part/%s-"%n+str(part_n)+".jpg")
    return


x=1
while (x<100):
    image = Image.open("./data/bin_img/binary_%s.jpg"%x)
    n=1
    x_size, y_size = image.size
    visit = [[0 for y in range(y_size)] for x in range(x_size)]
    for j in range(y_size):
        for i in range(x_size):
            if (visit[i][j] == 0 and image.getpixel((i,j)) <50):
                visit[i][j] = 1
                q.put((i,j))
                width=bfs(visit,image,n)
                cut(width[1]-width[0]+1,y_size,x,n,width[0])
                n=n+1


    print("finish%s"%x)
    x=x+1