# svm训练分类器
from sklearn import svm
from get_feature import *

# 0号验证码无0,1,I,L,O和小写字母
# 1号验证码无0,1,I,O,Z和小写字母
# 2号验证码无c,k,o,v,w,x,I,O
if __name__ == '__main__':
	lst = [ '2', '3', '4', '5', '6', '7', '8', '9','A','B','C','D','E','F','G',
			'H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y'] # 训练字符集
	X, Y = get_feature_set(lst) # 特征提取
	# print(X)
	clf = svm.LinearSVC()
	clf.fit(X,Y)
	Z, T= get_test_set(lst) # 测试准确率
	# print(Z)
	P = clf.predict(Z)
	P = P.tolist()
	# print(P)
	right = 0
	for i in range(len(P)):
		if P[i] == T[i]: right += 1
	print('Accuracy : ' + str(float(right)/float(len(P))))