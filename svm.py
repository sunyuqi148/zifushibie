from sklearn import svm
import json
import numpy as mp
from get_feature import *


if __name__ == '__main__':
	X = get_feature_set()
	
	f = open('./data/tag.list','r')
	s = f.readline()
	print(X)
	Y = list(s.split(' '))
	print(Y)
	f.close()

	clf = svm.SVC()
	clf.fit(X,Y)
	
	p = clf.predict(get_feature('./data/dataset/1 (7).jpg'))
	print(p.tolist())