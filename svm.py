from sklearn import svm
import json
import numpy as np
from get_feature import *



if __name__ == '__main__':
	lst = [ '2', '3', '4', '5', '6', '7', '8', '9']
	X, Y = get_feature_set(lst) #= np.array(get_feature_set())
	
	#f = open('./data/tag.list','r')
	#s = f.readline()
	#f.close()
	print(X)
	#Y = list(s.split(' '))
	#print(Y)

	clf = svm.LinearSVC()
	clf.fit(X,Y)
	
	Z, T= get_test_set(lst) #z=np.array(get_feature('./data/dataset/1 (7).jpg'))
	#z.reshape(-1,1)
	print(Z)
	P = clf.predict(Z)
	P = P.tolist()
	print(P)
	right = 0
	for i in range(len(P)):
		if P[i] == T[i]: right += 1
	print('Accuracy : ' + str(float(right)/float(len(P))))