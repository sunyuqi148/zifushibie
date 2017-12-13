从简至难的验证码识别：
get_img.py 从网站上获取验证码图片

level 0:1位无噪验证码的识别，来源botzone：http://www.botzone.org/captcha/digit?0.33774116522644837
img_binary0.py 二值化处理
recognize0.py 对一张原始图片进行识别，输出结果

level 1:4位无粘连验证码的识别，来源中国知网：http://my.cnki.net/elibregister/CheckCode.aspx?id=1511954726092
img_binary1.py 二值化处理
cut1.py 图片切割获取单个字符
recognize1.py 对一张原始图片进行识别，输出结果

level 2:4位有噪含干扰线验证码的识别，来源新东方：https://login.koolearn.com/sso/genVerifyImage.do
img_binary2.py 二值化处理
cut2.py 图片切割获取单个字符
recognize2.py 对一张原始图片进行识别，输出结果

level 3:不定位粘连双字体有噪含干扰线验证码的识别，来源163邮箱：http://reg.email.163.com/unireg/call.do?cmd=register.verifyCode&amp;v=common/verifycode/vc_en&amp;vt=main_acode&amp;env=402332522293&amp;t=1511248695493
img_binary3.py 二值化处理
del_line.py 去除干扰线
由于该验证码难度过大，未能完成后续工作