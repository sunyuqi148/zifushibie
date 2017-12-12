# 从网上下载数据集
import urllib
import urllib.request

def get_image(url,x): # 从网址url上下载编号为x的图片
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('./data/org_img/%s.jpg'%x,'wb') as fp:
        fp.write(get_img)
        print('download%s'%x)
    return

# http://www.botzone.org/captcha/digit?0.33774116522644837 1位无噪验证码
# http://my.cnki.net/elibregister/CheckCode.aspx?id=1511954726092 4位无粘连有噪验证码
# https://login.koolearn.com/sso/genVerifyImage.do 4位有噪含干扰线验证码
# http://reg.email.163.com/unireg/call.do?cmd=register.verifyCode&amp;v=common/verifycode/vc_en&amp;vt=main_acode&amp;
# env=402332522293&amp;t=1511248695493' 不定位粘连双字体有噪含干扰线验证码
url = 'https://login.koolearn.com/sso/genVerifyImage.do'
count=0
while count<100:
    get_image(url,count)
    count=count+1
