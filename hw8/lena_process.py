from skimage import io
import math
import os
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

def Opening_then_closing(img, kernel):

	return Closing(Opening(img, kernel), kernel)

def Closing_then_opening(img, kernel):
	
	return Opening(Closing(img, kernel), kernel)

def Median(lst):
	n = len(lst)
	s = sorted(lst)
	return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def Median_filter(img, size):
	
	height, width = img.shape[:2]
	new_img = img.copy()
	filter = np.zeros((size*size, 2), dtype=int)
	win = int(size/2)
	for i in range(size):
		for j in range(size):
			filter[size*i+j] = i - win, j - win
	
	for i in range(height):
		for j in range(width):
			filter_applied = [i, j] + filter
			lst = []
			for r, c in filter_applied:
				r = 0 if r < 0 else r
				c = 0 if c < 0 else c
				r = height-1 if r >= height else r
				c = width-1 if c >= width else c
				lst.append(img[r, c])
			new_img[i, j] = int(Median(lst))
	
	return new_img


def Box_filter(img, size):
	
	height, width = img.shape[:2]
	new_img = img.copy()
	filter = np.zeros((size*size, 2), dtype=int)
	win = int(size/2)
	for i in range(size):
		for j in range(size):
			filter[size*i+j] = i - win, j - win
	
	for i in range(height):
		for j in range(width):
			filter_applied = [i, j] + filter
			sum, cnt = 0. , 0
			for r, c in filter_applied:
				r = 0 if r < 0 else r
				c = 0 if c < 0 else c
				r = height-1 if r >= height else r
				c = width-1 if c >= width else c
				sum += img[r][c]
				cnt += 1
			new_img[i, j] = int(round(sum/cnt))
	
	return new_img


def Generate_noise(img, mode, intensity):
	
	height, width = img.shape[:2]
	noise_img = np.zeros((height, width), dtype = 'uint8')

	if mode == 'Gaussian':
		for i in range(height):
			for j in range(width):
				noise_img[i, j] = img[i, j] + intensity * np.random.normal(0., 1.)

		noise_img[noise_img[i, j] >= 255] = 255

	elif mode == 'SaltnPepper':
		for i in range(height):
			for j in range(width):
				rand = np.random.uniform(0., 1.)
				if(rand < intensity):
					noise_img[i, j] = 0
				elif(rand > (1 - intensity)):
					noise_img[i, j] = 255
				else:
					noise_img[i, j] = img[i, j]
	return noise_img

def main():
	
	lena = io.imread('lena.bmp')
	lena_gau10 = io.imread('lena_gau10.png')
	
	lena_gau10 = Generate_noise(lena, 'Gaussian', 10)
	lena_gau30 = Generate_noise(lena, 'Gaussian', 30)
	lena_sp01 = Generate_noise(lena, 'SaltnPepper', 0.1)
	lena_sp005 = Generate_noise(lena, 'SaltnPepper', 0.05)
	io.imsave('lena_gau10.png', lena_gau10)
	io.imsave('lena_gau30.png', lena_gau30)
	io.imsave('lena_sp01.png', lena_sp01)
	io.imsave('lena_sp005.png', lena_sp005)
	
	io.imsave("box_filter3X3_on_gau10.png", Box_filter(lena_gau10, 3))
	
	io.imsave("box_filter5X5_on_gau10.png", Box_filter(lena_gau10, 5))
	io.imsave("box_filter3X3_on_gau30.png", Box_filter(lena_gau30, 3))
	io.imsave("box_filter5X5_on_gau30.png", Box_filter(lena_gau30, 5))
	io.imsave("box_filter3X3_on_sp005.png", Box_filter(lena_sp005, 3))
	io.imsave("box_filter5X5_on_sp005.png", Box_filter(lena_sp005, 5))
	io.imsave("box_filter3X3_on_sp01.png", Box_filter(lena_sp01, 3))
	io.imsave("box_filter5X5_on_sp01.png", Box_filter(lena_sp01, 5))
	
	io.imsave("med_filter3X3_on_gau10.png", Median_filter(lena_gau10, 3))
	io.imsave("med_filter5X5_on_gau10.png", Median_filter(lena_gau10, 5))
	io.imsave("med_filter3X3_on_gau30.png", Median_filter(lena_gau30, 3))
	io.imsave("med_filter5X5_on_gau30.png", Median_filter(lena_gau30, 5))
	io.imsave("med_filter3X3_on_sp005.png", Median_filter(lena_sp005, 3))
	io.imsave("med_filter5X5_on_sp005.png", Median_filter(lena_sp005, 5))
	io.imsave("med_filter3X3_on_sp01.png", Median_filter(lena_sp01, 3))
	io.imsave("med_filter5X5_on_sp01.png", Median_filter(lena_sp01, 5))

	# Octagonal 3-5-5-5-3 kernel
	kernel = np.array([[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]])

	io.imsave("closing_then_opening_on_gau10.png", Closing_then_opening(lena_gau10, kernel))
	io.imsave("closing_then_opening_on_gau30.png", Closing_then_opening(lena_gau30, kernel))
	io.imsave("closing_then_opening_on_sp005.png", Closing_then_opening(lena_sp005, kernel))
	io.imsave("closing_then_opening_on_sp01.png", Closing_then_opening(lena_sp01, kernel))
	io.imsave("opening_then_closing_on_gau10.png", Opening_then_closing(lena_gau10, kernel))
	io.imsave("opening_then_closing_on_gau30.png", Opening_then_closing(lena_gau30, kernel))
	io.imsave("opening_then_closing_on_sp005.png", Opening_then_closing(lena_sp005, kernel))
	io.imsave("opening_then_closing_on_sp01.png", Opening_then_closing(lena_sp01, kernel))
	
	lena = lena / 256
	namelist = os.listdir(".")
	mu = np.sum(lena) / lena.size
	VS = np.sum(np.power(lena - mu, 2)) / lena.size

	for i in namelist:
		if(not '.png' in i):
			continue
		temp = io.imread(i)
		temp = temp/256
		mu_N = np.sum(temp - lena) / temp.size
		VN = np.sum(np.power(temp - lena - mu_N, 2)) / temp.size
		# print(temp - lena - mu_N)
		SNR = 20 * math.log10(math.sqrt(VS) / math.sqrt(VN))
		print('({})  SNR:{}'.format(i, SNR))
	
	
if __name__ == '__main__':
	main()
