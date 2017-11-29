import urllib
import urllib.request

def get_image(url,x):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('./data/org_img/%s.jpg'%x,'wb') as fp:
        fp.write(get_img)
        print('download%s'%x)
    return

#http://www.botzone.org/captcha/digit?0.33774116522644837
#http://my.cnki.net/elibregister/CheckCode.aspx?id=1511954726092
#https://www.imooc.com/passport/user/verifycode?t=1511959477881
url = 'https://www.imooc.com/passport/user/verifycode?t=1511959477881'
count=1
while count<100:
    get_image(url,count)
    count=count+1