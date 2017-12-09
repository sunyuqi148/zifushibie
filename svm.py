from sklearn import svm
import json
import numpy as np
from get_feature import *

if __name__ == '__main__':
	lst = [ '2', '3', '4', '5', '6', '7', '8', '9','A','B','C','D','E','F','G',
			'H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y']
	X, Y = get_feature_set(lst)

	# print(X)

	clf = svm.LinearSVC()
	clf.fit(X,Y)
	
	Z, T= get_test_set(lst)
	# print(Z)
	P = clf.predict(Z)
	P = P.tolist()
	# print(P)
	right = 0
	for i in range(len(P)):
		if P[i] == T[i]: right += 1
	print('Accuracy : ' + str(float(right)/float(len(P))))