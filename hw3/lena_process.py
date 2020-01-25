from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2

def Intensity_division(img, intensity):

	for i in range(len(img)):
		for j in range(len(img)):
			img[i][j] = round(img[i][j]/3)
	
	return img

def Plot_histogram(img, name):
	pixels = np.zeros((256), dtype = int)

	for row in img:
		for i in row:
			pixels[i] += 1
	
	plt.bar(range(len(pixels)), pixels)
	plt.title('Histogram of ' + name)
	plt.xlabel('Gray scale value')
	plt.ylabel('Frenquency')
	plt.savefig(name + '_histogram.png', dpi=130)
	plt.clf()
	return pixels

def Histogram_equalization(img, his):
	
	# Linearization
	cdf = np.zeros((256), dtype = int)
	sum = 0

	for i in range(len(his)):
		sum += his[i]
		cdf[i] = sum

	# Transformation
	img_equalized = img.copy()
	for i in range(len(img)):
		for j in range(len(img)):
			img_equalized[i][j] = round(255 * cdf[img[i][j]]/sum)

	return img_equalized

def main():
	
	img = io.imread('lena.bmp')
	his = Plot_histogram(img, 'lena')
	io.imsave('lena.png', img)
	
	img_divided = Intensity_division(img, 3)
	his_divided = Plot_histogram(img_divided, 'lena_divided')
	io.imsave('lena_divided.png', img_divided)
	
	img_equalized = Histogram_equalization(img_divided, his_divided)
	his_eqaulized = Plot_histogram(img_equalized, 'lena_equalized')
	io.imsave('lena_equalized.png', img_equalized)
	


if __name__ == '__main__':
	main()
