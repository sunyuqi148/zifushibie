import urllib
import urllib.request

def get_image(url,x):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('./data/%s.jpg'%x,'wb') as fp:
        fp.write(get_img)
        print('download%s'%x)
    return

#<img id="vcodeImg" class="vCode" style="cursor:pointer;" src="/unireg/call.do?cmd=register.verifyCode&amp;v=common/verifycode/vc_en&amp;vt=main_acode&amp;env=402332522293&amp;t=1511248695493" alt="验证码" width="120" height="50">
url = 'http://reg.email.163.com/unireg/call.do?cmd=register.verifyCode&amp;v=common/verifycode/vc_en&amp;vt=main_acode&amp;env=402332522293&amp;t=1511248695493'
count=1
while count<100:
    get_image(url,count)
    count=count+1