from skimage import io
import numpy as np	

def Binarize(img, intensity):
	
	# Binarize image
	img_binarized = img.copy()
		
	for i in range(img_binarized.shape[0]):
		for j in range(img_binarized.shape[1]):
			if img_binarized[i][j] >= intensity:
				img_binarized[i][j] = 255
			else:
				img_binarized[i][j] = 0
		
	return img_binarized	

def Downsampling(img, size):
	
	img_down = np.zeros((int(img.shape[0]/size), int(img.shape[1]/size)), dtype = int)
	
	for i in range(img_down.shape[0]):
		for j in range(img_down.shape[1]):
			img_down[i][j] = img[i*size][j*size]
	
	return img_down

def h(b, c, d, e):

	if b == c:
		if d != b or e != b:	# q
			return 1
		if d == b and e == b:	# r
			return 2
	else:						# s
		return 0

def f(a_1, a_2, a_3, a_4):
	if a_1 == a_2 and a_2 == a_3 and a_3 == a_4 and a_4 == 2:
		return 5
	else:
		return [a_1, a_2, a_3, a_4].count(1)

def Yokoi(img):
	
	height, width = img.shape[:2]
	yokoi = np.zeros((height, width), dtype = int)
	bin_img = img.copy()
	bin_img[bin_img == 255] = 1
	connectivity = 4
	neighbors = np.array([[(0, 0), (0, 1), (-1, 1), (-1, 0)],
						[(0, 0), (-1, 0), (-1, -1), (0, -1)],
						[(0, 0), (0, -1), (1, -1), (1, 0)],
						[(0, 0), (1, 0), (1, 1), (0, 1)]])

	h_table = np.zeros((2, 2, 2, 2))

	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					h_table[b, c, d, e] = h(b, c, d, e)

	
	# Compute h(b, c, d, e)
	for i in range(height):
		for j in range(width):
			
			if bin_img[i, j] == 0:
				continue

			f_input = []
			for k in neighbors:
  				
				idx = (i, j) + k
				bin_value = []
				for m, n in idx:
					if m < 0 or n < 0 or n >= height or m >= width:
						bin_value.append(0)
					else:
						bin_value.append(bin_img[m, n])
				
				f_input.append(h_table[bin_value[0], bin_value[1], bin_value[2], bin_value[3]])
			
			yokoi[i][j] = f(f_input[0], f_input[1], f_input[2], f_input[3])
				
	return yokoi

def Pair_relationship(yokoi):
	
	marked_img = np.zeros((yokoi.shape[0], yokoi.shape[1]), dtype = int)
	height, width = yokoi.shape[:2]

	for i in range(height):
		for j in range(width):
			
			if yokoi[i][j] == 0:
				continue
			if yokoi[i][j] != 1:
				marked_img[i][j] = 1
				continue

			is_p = False
			for m, n in [(0, 1), (-1, 0), (0, -1), (1, 0)]:

				if i+m < 0 or j+n < 0 or i+m >= height or j+n >= width:
					continue

				if yokoi[i+m][j+n] == 1:
					# Mark as p
					marked_img[i][j] = 2
					is_p = True
					break
			if not is_p:
				# Mark as q
				yokoi[i][j] = 1

	return marked_img

def Thinning(img):
	
	height, width = img.shape[:2]
	bin_img = img.copy()
	bin_img = (bin_img/255).astype(int)
	neighbors = np.array([[(0, 0), (0, 1), (-1, 1), (-1, 0)],
						[(0, 0), (-1, 0), (-1, -1), (0, -1)],
						[(0, 0), (0, -1), (1, -1), (1, 0)],
						[(0, 0), (1, 0), (1, 1), (0, 1)]])


	yokoi = Yokoi(img)
	marked_img = Pair_relationship(yokoi)

	# Connected Shrink


	for i in range(height):
		for j in range(width):
			
			if marked_img[i][j] != 2:
				continue

			cnt = 0
			for k in neighbors:
  					
				idx = (i, j) + k
				bin_value = []
				for m, n in idx:
					if m < 0 or n < 0 or n >= height or m >= width:
						bin_value.append(0)
					else:
						bin_value.append(bin_img[m, n])
				
				if h(bin_value[0], bin_value[1], bin_value[2], bin_value[3]) == 1:
					cnt += 1
			
			if cnt == 1:
				img[i][j] = 0
				bin_img[i][j] = 0	
	
	return img


def main():
	
	lena = io.imread('lena.bmp')
	lena_binarized = Binarize(lena, 128)
	lena_down = Downsampling(lena_binarized, 8)
	io.imsave('lena_down.png', lena_down)
	lena_thinning = lena_down.copy()
	
	iters = 7
	for i in range(iters):
		lena_thinning = Thinning(lena_thinning)
	io.imsave('lena_thinning.png', lena_thinning)

	

	
if __name__ == '__main__':
	main()
