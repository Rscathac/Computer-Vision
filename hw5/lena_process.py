from skimage import io
import numpy as np


def Erosion(img, kernel):

	r = int((kernel.shape[0]-1)/2)
	
	new_img = img.copy()
	height, width = img.shape[:2]
	
	for i in range(height):
		for j in range(width):
			local_min = 255
			for h in range(-r, r+1):
				for w in range(-r, r+1):
					if (i+h) < 0 or (i+h) >= height or (j+w) < 0 or (j+w) >= width or kernel[h+r][w+r] == 0:
						continue
					
					if img[i+h][j+w] < local_min:
						local_min = img[i+h][j+w]

			
			new_img[i][j] = local_min
	
	return new_img


def Dilation(img, kernel):
	
	r = int((kernel.shape[0]-1)/2)
	
	new_img = img.copy()
	height, width = img.shape[:2]
	
	for i in range(height):
		for j in range(width):
			local_max = 0
			for h in range(-r, r+1):
				for w in range(-r, r+1):
					if (i-h) < 0 or (i-h) >= height or (j-w) < 0 or (j-w) >= width or kernel[h+r][w+r] == 0:
						continue
					
					if img[i-h][j-w] > local_max:
						local_max = img[i-h][j-w]

			
			new_img[i][j] = local_max
	
	return new_img

def Opening(img, kernel):
	
	return(Dilation(Erosion(img, kernel), kernel))

def Closing(img, kernel):
	
	return(Erosion(Dilation(img, kernel), kernel))


def main():
	
	lena = io.imread('lena.bmp')
	
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
	
	
	
if __name__ == '__main__':
	main()
