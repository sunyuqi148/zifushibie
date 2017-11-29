import urllib
import urllib.request
import time

def get_image(url,x):# 下载url网站的图片
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('%s.jpg'%x,'wb') as fp:
        fp.write(get_img)
        print('download%s'%x)
    return

#不需修改以上部分
#<img id="vcodeImg" class="vCode" style="cursor:pointer;" src="/unireg/call.do?cmd=register.verifyCode&amp;v=common/verifycode/vc_en&amp;vt=main_acode&amp;env=402332522293&amp;t=1511248695493" alt="验证码" width="120" height="50">
url = 'http://reg.email.163.com/unireg/call.do?cmd=register.verifyCode&amp;v=common/verifycode/vc_en&amp;vt=main_acode&amp;env=402332522293&amp;t=1511248695493'
count=1 # 从某张图片开始，自己设定，以免重名
while count<100:# 注意该网站用同一IP地址最多爬取99张图片，之后将禁止访问！
    get_image(url,count)
    count=count+1