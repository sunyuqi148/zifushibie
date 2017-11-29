from PIL import Image, ImageDraw

def tuple_equal(x, y):
	#print(x)
	#print(y)
	#print()
	tmp = 0
	for i in range(3):
		tmp += abs(x[i] - y[i])
	if tmp > 15 : return True
	return False

def extract_letter(filename, outfilename = 'extract.jpg'):
	img = Image.open(filename)
	width, height = img.size
	out = Image.new('RGB', (width, height), (255, 255, 255))
	draw = ImageDraw.Draw(out)
	for x in range(height):
		for y in range(width):
			if y == 0 : continue
			#print(str(x)+' '+str(y))
			if tuple_equal(img.getpixel((y, x)), img.getpixel((y-1, x))):
				draw.point((y, x), fill = 0)
	out.save(outfilename)
	return out
	
for i in range(49):
	x = extract_letter('./data/org_img/' + str(i+1) + '.jpg', './data/bin_img/' + str(i+1) + '.jpg')
#x = extract_letter('0.png', '0.jpg')
#x.show()