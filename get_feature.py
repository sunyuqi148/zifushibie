# 提取特征与图片等
from PIL import Image
from sklearn.decomposition import PCA
import numpy as np
import os

def tuple_zero(x):
	for i in range(3):
		if x[i]!=0: return False
	return True

def get_feature(filename): # 找到图中的黑像素，提取到一个特征向量中
	img = Image.open(filename)
	width, height = img.size
	feature = []
	for y in range(25):
		pix_cnt_x = 0
		for x in range(width):
			if y >= height: break
			if img.getpixel((x,y))<20:
				pix_cnt_x += 1
		feature.append(pix_cnt_x)
	for x in range(15):
		pix_cnt_y = 0
		for y in range(height):
			if x >= width : break
			if img.getpixel((x,y))<20:
				pix_cnt_y += 1
		feature.append(pix_cnt_y)
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
	
def get_feature_set(cset, k = 20): # 获取训练字符集
	fset = []
	Y = []
	for c in cset:
		root = './data/classify2/'+c+'/'
		for idx, jpg in enumerate(os.listdir(root)):
			# if idx >= k: break
			filename = os.path.join(root, jpg)
			fset.append(get_feature(filename))
			Y.append(c)
	return np.array(fset), Y
	
def get_test_set(cset, k = 20): # 获取测试字符集
	fset = []
	Y = []
	for c in cset:
		root = './data/classify2/'+c+'/'
		for idx, jpg in enumerate(os.listdir(root)):
			if idx <= k: continue
			filename = os.path.join(root, jpg)
			fset.append(get_feature(filename))
			Y.append(c)
	return np.array(fset), Y

def get_symbol(): # 获取单个图片的符号内容
	fset = []
	root = './data/part'
	for idx, jpg in enumerate(os.listdir(root)):
		filename = os.path.join(root, jpg)
		fset.append(get_feature(filename))
	return np.array(fset)
