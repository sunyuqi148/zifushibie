from PIL import Image
from sklearn.decomposition import PCA
import numpy as np
import os

def tuple_zero(x):
	tmp = 0
	for i in range(3):
		if x[i]!=0: return False
	return True

def get_feature(filename):
	img = Image.open(filename)
	width, height = img.size
	print(str(width) + ' ' + str(height))
	#exit()

	feature = []
	for y in range(25):
		pix_cnt_x = 0
		for x in range(width):
			if y >= height: break
			if img.getpixel((x,y))==0: #tuple_zero(img.getpixel((x,y))):
				pix_cnt_x += 1
		feature.append(pix_cnt_x)
	for x in range(15):
		pix_cnt_y = 0
		for y in range(height):
			if x >= width : break
			if img.getpixel((x,y))==0:
				pix_cnt_y += 1
		feature.append(pix_cnt_y)
	print(feature)
	return feature

def feature_PCA(feature_set, k = 10, filename = ''):
	pca = PCA(n_components = k)
	X = np.array(feature_set)
	Y = pca.fit_transform(X)
	if len(filename) != 0:
		f = open(filename, 'w')
		f.write(json.dumps(Y))
		f.close()
	return Y.tolist()
	
def get_feature_set(cset, k = 20):
	fset = []
	Y = []
	for c in cset:
		root = './data/dataset/'+c+'/'
		for idx, jpg in enumerate(os.listdir(root)):
			if idx > k: break
			filename = os.path.join(root, jpg)
			#print(filename)
			fset.append(get_feature(filename))
			Y.append(c)
	return np.array(fset), Y
	
def get_test_set(cset, k = 20):
	fset = []
	Y = []
	for c in cset:
		root = './data/dataset/'+c+'/'
		for idx, jpg in enumerate(os.listdir(root)):
			if idx <= k: continue
			filename = os.path.join(root, jpg)
			fset.append(get_feature(filename))
			Y.append(c)
	return np.array(fset), Y 
