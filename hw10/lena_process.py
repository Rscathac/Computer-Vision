from skimage import io
import math
import os
import numpy as np

def Border_padding(img , size):
	
	height, width = img.shape
	win = int(size/2)
	r = win*2
	new_img = np.zeros((height+r, width+r), dtype=int)
	new_height, new_width = new_img.shape

	for i in range(height):
		for j in range(width):
			new_img[i+win][j+win] = img[i][j]

	for i in range(height):
		new_img[i+win, :win] = img[i][0]
		new_img[i+win, -win:] = img[i][width-1]
	for i in range(width):
		new_img[:win, i+win] = img[0][i]
		new_img[-win:, i+win] = img[height-1][i]
	new_img[:win, :win] = img[0][0]
	new_img[:win, -win:] = img[0][width-1]
	new_img[-win:, :win] = img[height-1][0]
	new_img[-win:, -win:] = img[height-1][width-1]
	return new_img


def Laplacian_type1(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 3)
	win = 1
	height, width = new_img.shape
	marked_img = np.zeros((height, width), dtype=int)

	# Compute Laplacian value
	for i in range(height):
		for j in range(width):
			r, c = i+win, j+win
			laplacian = padded_img[r-1][c] + padded_img[r][c-1] + (-4)*padded_img[r][c] + padded_img[r][c+1] + padded_img[r+1][c]
			if laplacian >= threshold:
				marked_img[i][j] = 1
			elif laplacian <= -threshold:
				marked_img[i][j] = -1
			else:
				marked_img[i][j] = 0
	
	# Zero Crossing
	for i in range(height):
		for j in range(width):
			new_img[i][j] = 255
			if marked_img[i][j] != 1:
				continue
			
			cross = False
			for r in [-1, 0, 1]:
				for c in [-1, 0, 1]:
					if i+r < 0 or i+r >= height or j+c < 0 or j+c >= width or cross:
						continue
					if marked_img[i+r][j+c] == -1:
						new_img[i][j] = 0
						cross = True
	return new_img

def Laplacian_type2(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 3)
	win = 1
	height, width = new_img.shape
	marked_img = np.zeros((height, width), dtype=int)

	# Compute Laplacian value
	for i in range(height):
		for j in range(width):
			r, c = i+win, j+win
			laplacian = padded_img[r-1][c-1] + padded_img[r-1][c] + padded_img[r-1][c+1] + padded_img[r][c-1] + (-8)*padded_img[r][c] + padded_img[r][c+1] + padded_img[r+1][c-1] + padded_img[r+1][c] + padded_img[r+1][c+1]
			laplacian = laplacian * (1/3)
			if laplacian >= threshold:
				marked_img[i][j] = 1
			elif laplacian <= -threshold:
				marked_img[i][j] = -1
			else:
				marked_img[i][j] = 0
	
	# Zero Crossing
	for i in range(height):
		for j in range(width):
			new_img[i][j] = 255
			if marked_img[i][j] != 1:
				continue
			
			cross = False
			for r in [-1, 0, 1]:
				for c in [-1, 0, 1]:
					if i+r < 0 or i+r >= height or j+c < 0 or j+c >= width or cross:
						continue
					if marked_img[i+r][j+c] == -1:
						new_img[i][j] = 0
						cross = True
	return new_img

def Minimum_Laplacian(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 3)
	win = 1
	height, width = new_img.shape
	marked_img = np.zeros((height, width), dtype=int)

	# Compute Laplacian value
	for i in range(height):
		for j in range(width):
			r, c = i+win, j+win
			laplacian = 2*padded_img[r-1][c-1] - padded_img[r-1][c] + 2*padded_img[r-1][c+1] - padded_img[r][c-1] - 4*padded_img[r][c] - padded_img[r][c+1] + 2*padded_img[r+1][c-1] - padded_img[r+1][c] +2* padded_img[r+1][c+1]
			laplacian = laplacian * (1/3)
			if laplacian >= threshold:
				marked_img[i][j] = 1
			elif laplacian <= -threshold:
				marked_img[i][j] = -1
			else:
				marked_img[i][j] = 0
	
	# Zero Crossing
	for i in range(height):
		for j in range(width):
			new_img[i][j] = 255
			if marked_img[i][j] != 1:
				continue
			
			cross = False
			for r in [-1, 0, 1]:
				for c in [-1, 0, 1]:
					if i+r < 0 or i+r >= height or j+c < 0 or j+c >= width or cross:
						continue
					if marked_img[i+r][j+c] == -1:
						new_img[i][j] = 0
						cross = True
	return new_img

def Laplacian_of_Gaussian(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 11)
	win = 5
	height, width = new_img.shape
	marked_img = np.zeros((height, width), dtype=int)
	kernel = [
		[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0], 
		[0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0], 
		[0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0], 
		[-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1], 
		[-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1], 
		[-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2],
		[-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
		[-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
		[0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0], 
		[0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
		[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]
	]

	# Compute Laplacian value
	for i in range(height):
		for j in range(width):
			laplacian = 0
			for r in range(-5, 6):
				for c in range(-5, 6):
					laplacian += padded_img[i+r][j+c] * kernel[r+win][c+win]
			
			if laplacian >= threshold:
				marked_img[i][j] = 1
			elif laplacian <= -threshold:
				marked_img[i][j] = -1
			else:
				marked_img[i][j] = 0
	
	# Zero Crossing
	for i in range(height):
		for j in range(width):
			new_img[i][j] = 255
			if marked_img[i][j] != 1:
				continue
			
			cross = False
			for r in [-1, 0, 1]:
				for c in [-1, 0, 1]:
					if i+r < 0 or i+r >= height or j+c < 0 or j+c >= width or cross:
						continue
					if marked_img[i+r][j+c] == -1:
						new_img[i][j] = 0
						cross = True
	return new_img

def Difference_of_Gaussian(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 11)
	win = 5
	height, width = new_img.shape
	marked_img = np.zeros((height, width), dtype=int)
	kernel = [
		[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1], 
		[-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3], 
		[-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4], 
		[-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6], 
		[-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7], 
		[-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8],
		[-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
		[-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
		[-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
		[-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
		[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1], 
	]


	# Compute Laplacian value
	for i in range(height):
		for j in range(width):
			laplacian = 0
			for r in range(-5, 6):
				for c in range(-5, 6):
					laplacian += padded_img[i+r][j+c] * kernel[r+win][c+win]
			
			if laplacian >= threshold:
				marked_img[i][j] = 1
			elif laplacian <= -threshold:
				marked_img[i][j] = -1
			else:
				marked_img[i][j] = 0
	
	# Zero Crossing
	for i in range(height):
		for j in range(width):
			new_img[i][j] = 255
			if marked_img[i][j] != 1:
				continue
			
			cross = False
			for r in [-1, 0, 1]:
				for c in [-1, 0, 1]:
					if i+r < 0 or i+r >= height or j+c < 0 or j+c >= width or cross:
						continue
					if marked_img[i+r][j+c] == -1:
						new_img[i][j] = 0
						cross = True
	return new_img

def main():

	lena = io.imread('lena.bmp')
	io.imsave("laplacian_1.png", Laplacian_type1(lena, 15))
	io.imsave("laplacian_2.png", Laplacian_type2(lena, 15))	
	io.imsave("min_laplacian.png", Minimum_Laplacian(lena, 20))
	io.imsave("LOG.png", Laplacian_of_Gaussian(lena, 3000))
	io.imsave("DOG.png", Difference_of_Gaussian(lena, 1))
	
if __name__ == '__main__':
	main()
