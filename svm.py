from sklearn import svm
import json
import numpy as np
from get_feature import *


if __name__ == '__main__':
	X = np.array(get_feature_set())
	
	f = open('./data/tag.list','r')
	s = f.readline()
	f.close()
	print(X)
	Y = list(s.split(' '))
	print(Y)

	clf = svm.LinearSVC()
	clf.fit(X,Y)
	
	z=np.array(get_feature('./data/dataset/1 (7).jpg'))
	z.reshape(-1,1)
	print(z)
	p = clf.predict([z])
	print(p.tolist())