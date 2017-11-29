from PIL import Image
from sklearn.decomposition import PCA


def tuple_zero(x):
	tmp = 0
	for i in range(3):
		if x[i]!=0: return False
	return True

def get_feature(filename):
	img = Image.open(filename)
	width, height = img.size
	feature = []
	for y in range(height):
		pix_cnt_x = 0
		for x in range(width):
			z = img.getpixel((x,y))
		#	print(z)
			if tuple_zero(img.getpixel((x,y))):
				pix_cnt_x += 1
		feature.append(pix_cnt_x)
	for x in range(width):
		pix_cnt_y = 0
		for y in range(height):
			if img.getpixel((x,y))==0:
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
	
def get_feature_set(k = 6):
	fset = []
	for i in range(k):
		fset.append(get_feature('./data/dataset/1 ('+ str(i+1) + ').jpg'))
	return fset
