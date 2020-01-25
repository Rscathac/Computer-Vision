from skimage import io
import numpy as np

def Binarize(img, intensity):
	
	# Binarize image
	lena_binarized = img.copy()

	for i in range(len(lena_binarized)):
		for j in range(len(lena_binarized)):
			if lena_binarized[i][j] >= intensity:
				lena_binarized[i][j] = 255
			else:
				lena_binarized[i][j] = 0

	return lena_binarized

def Erosion(img, kernel):

	cover = kernel.copy()
	kernel = kernel.copy() * 255
	r = int((kernel.shape[0]-1)/2)
	
	height, width = img.shape[:2]
	new_img = np.zeros((height, width), dtype='uint8')

	for i in range(height):
		for j in range(width):
#			if img[i][j] == 0:
#				continue

			if i-r < 0 or i+r >= height or j-r < 0 or j+r >= width:
				continue
			
			if (np.multiply(img[i-r:i+r+1, j-r:j+r+1], cover) == kernel).all():
				new_img[i][j] = 255
	
	return new_img

def Dilation(img, kernel):
	
	kernel = kernel.copy() * 255
	r = int((kernel.shape[0]-1)/2)
	
	new_img = img.copy()
	height, width = img.shape[:2]
	
	for i in range(height):
		for j in range(width):
			if img[i][j] == 0:
				continue
			
			for h in range(-r, r+1):
				for w in range(-r, r+1):
					if (i+h) < 0 or (i+h) >= height or (j+w) < 0 or (j+w) >= width:
						continue
					
					if new_img[i+h][j+w] == 0:
						new_img[i+h][j+w] = kernel[h+r][w+r]
	
	return new_img

def Opening(img, kernel):
	
	return(Dilation(Erosion(img, kernel), kernel))

def Closing(img, kernel):
	
	return(Erosion(Dilation(img, kernel), kernel))

def Hit_and_miss_transform(img, J, K):
	
	A_J = Erosion(img, J)
	Ac_K = Erosion(255 - img , K)
	new_img = np.zeros((img.shape), dtype='uint8')
	
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if (A_J[i][j] == Ac_K[i][j]) and (A_J[i][j] == 255):
				new_img[i][j] = 255
				
	
	return new_img

def main():
	
	lena = io.imread('lena.bmp')
	lena = Binarize(lena, 128)


	# Octagonal 3-5-5-5-3 kernel
	kernel = np.array([[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]])
	
	
	print('---Dilation start---')
	lena_dilation = Dilation(lena, kernel)
	io.imsave('lena_dilation.png', lena_dilation)
	print('---Dilation end---')
	
	
	print('---Erosion start---')
	lena_erosion = Erosion(lena, kernel)
	io.imsave('lena_erosion.png', lena_erosion)
	print('---Erosion end---')

	print('---Opening start---')
	lena_opening = Opening(lena, kernel)
	io.imsave('lena_opening.png', lena_opening)
	print('---Opening end---')

	print('---Closing start---')
	lena_closing = Closing(lena, kernel)
	io.imsave('lena_closing.png', lena_closing)
	print('---Closing end---')
	
	
	# Hit and Miss transformation's kernels
	J = np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]])
	K = np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]])
	print('---Hit and miss transformation start---')
	lena_hit_miss = Hit_and_miss_transform(lena, J, K)
	io.imsave('lena_hit_miss.png', lena_hit_miss)
	print('---Hit and miss transformation end---')


	
if __name__ == '__main__':
	main()
