from sklearn import svm
from get_feature import *
from img_binary2 import *
from cut2 import *
import os

lst = [ '0','1','2', '3', '4', '5', '6', '7', '8', '9','A','B','C','D','E','F','G',
				'H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z',
		        '_a','_b','_d','_e','_f','_g','_h','_i','_j','_l','_m','_n','_p','_q',
		        '_r','_s','_t','_u','_y','_z'] # 字符集
X, Y = get_feature_set(lst) #进行SVM分类
clf = svm.LinearSVC()
clf.fit(X,Y)
x=0 # 待识别的文件编号
while(x<100):
	img_binary2(x) # 二值化
	cut2(x) # 切割
	Z= get_symbol() # 获取单个字符图片
	P = clf.predict(Z) # 解析该图片
	P = P.tolist()
	os.remove("./data/bin_img/binary_%s.jpg"%x) # 删除生成的临时文件
	os.remove("./data/part/%s-1.jpg"%x)
	if (os.path.exists("./data/part/%s-2.jpg" % x)):
		os.remove("./data/part/%s-2.jpg" % x)
	if (os.path.exists("./data/part/%s-3.jpg" % x)):
		os.remove("./data/part/%s-3.jpg" % x)
	if(os.path.exists("./data/part/%s-4.jpg"%x)):
		os.remove("./data/part/%s-4.jpg"%x)
	if (os.path.exists("./data/part/%s-5.jpg" % x)):
		os.remove("./data/part/%s-5.jpg" % x)
	if (os.path.exists("./data/part/%s-6.jpg" % x)):
		os.remove("./data/part/%s-6.jpg" % x)
	print(x)
	print(P) # 输出结果
	x=x+1