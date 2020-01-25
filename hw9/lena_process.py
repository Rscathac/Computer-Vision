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

def Roberts(img, threshold):
	
	new_img = img.copy()
	padded_img = Border_padding(img, 2)
	win = 1
	height, width = new_img.shape
	
	for i in range(height):
		for j in range(width):
			r,c = i+win, j+win
			r1 = padded_img[r+1][c+1] - padded_img[r][c]
			r2 = padded_img[r+1][c] - padded_img[r][c+1]
			grad = (r1**2+r2**2)**(1/2)
			if grad >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img

def Prewitt(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 3)
	win = 1
	height, width = new_img.shape

	for i in range(height):
		for j in range(1, width):
			r, c = i+win, j+win
			p1 = (-1)*padded_img[r-1][c-1] + (-1)*padded_img[r-1][c] + (-1)*padded_img[r-1][c+1] + padded_img[r+1][c-1] + padded_img[r+1][c] + padded_img[r+1][c+1] 
			p2 = (-1)*padded_img[r][c-1] + (-1)*padded_img[r][c-1] + (-1)*padded_img[r+1][c-1] + padded_img[r-1][c+1] + padded_img[r][c+1] + padded_img[r+1][c+1] 
			grad = (p1**2+p2**2)**(1/2)
			if grad >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img

def Sobel(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 3)
	win = 1
	height, width = new_img.shape

	for i in range(height):
		for j in range(width):
			r, c = i+win, j+win
			s1 = (-1)*padded_img[r-1][c-1] + (-2)*padded_img[r-1][c] + (-1)*padded_img[r-1][c+1] + padded_img[r+1][c-1] + 2*padded_img[r+1][c] + padded_img[r+1][c+1] 
			s2 = (-1)*padded_img[r][c-1] + (-2)*padded_img[r][c-1] + (-1)*padded_img[r+1][c-1] + padded_img[r-1][c+1] + 2* padded_img[r][c+1] + padded_img[r+1][c+1] 
			grad = (s1**2+s2**2)**(1/2)
			if grad >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img

def Frei_and_Chen(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 3)
	win = 1
	height, width = new_img.shape

	for i in range(height):
		for j in range(width):
			r, c = i+win, j+win
			f1 = (-1)*padded_img[r-1][c-1] + (-1)*2**(1/2)*padded_img[r-1][c] + (-1)*padded_img[r-1][c+1] + padded_img[r+1][c-1] + 2**(1/2)*padded_img[r+1][c] + padded_img[r+1][c+1] 
			f2 = (-1)*padded_img[r][c-1] + (-1)*2**(1/2)*padded_img[r][c-1] + (-1)*padded_img[r+1][c-1] + padded_img[r-1][c+1] + 2**(1/2)*padded_img[r][c+1] + padded_img[r+1][c+1] 
			grad = (f1**2+f2**2)**(1/2)
			if grad >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img

def Kirsch(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 5)
	win = 2
	height, width = new_img.shape
	k = [-3, -3, -3, -3, -3, 5, 5, 5]

	for i in range(height):
		for j in range(width):
			k_list = []
			r, c = i+win, j+win
			for idx in range(8):
				k_list.append(padded_img[r - 1][c - 1] * k[idx % 8] + padded_img[r - 1][c] * k[(idx + 1) % 8] + padded_img[r - 1][c + 1] * k[(idx + 2) % 8]
				+ padded_img[r][c + 1] * k[(idx + 3) % 8] + padded_img[r + 1][c + 1] * k[(idx + 4) % 8]
				+ padded_img[r + 1][c] * k[(idx + 5) % 8] + padded_img[r + 1][c - 1] * k[(idx + 6) % 8] + padded_img[r][c - 1] * k[(idx + 7) % 8])
			
			if max(k_list) >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img

def Robinson(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 5)
	win = 2
	height, width = new_img.shape
	R = [-1, 0, 1, 2, 1, 0, -1, -2]

	for i in range(height):
		for j in range(width):
			r_list = []
			r, c = i+win, j+win
			for idx in range(8):
				r_list.append(padded_img[r - 1][c - 1] * R[idx % 8] + padded_img[r - 1][c] * R[(idx + 1) % 8] + padded_img[r - 1][c + 1] * R[(idx + 2) % 8]
				+ padded_img[r][c + 1] * R[(idx + 3) % 8] + padded_img[r + 1][c + 1] * R[(idx + 4) % 8]
				+ padded_img[r + 1][c] * R[(idx + 5) % 8] + padded_img[r + 1][c - 1] * R[(idx + 6) % 8] + padded_img[r][c - 1] * R[(idx + 7) % 8])
			
			if max(r_list) >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img

def Nevatia_Babu(img, threshold):

	new_img = img.copy()
	padded_img = Border_padding(img, 5)
	win = 2
	height, width = new_img.shape
	kernel = [[-2, -2], [-1, -2], [0, -2], [1, -2], [2, -2],[-2, -1], [-1, -1], [0, -1], [1, -1], [2, -1], 
			[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0],[-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1], [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2]] 
	g0 = [ 100, 100, 0, -100, -100, 100, 100, 0, -100, -100, 100, 100, 0, -100, -100, 100, 100, 0, -100, -100, 100, 100, 0, -100, -100]
	g1 = [ 100, 100, 100, 100, 100, 100, 100, 100, 78, -32, 100, 92, 0, -92, -100, 32, -78, -100, -100, -100, -100, -100, -100, -100, -100]
	g2 = [-100, -100, -100, -100, -100, 32, -78, -100, -100, -100, 100, 92, 0, -92, -100, 100, 100, 100, 78, -32, 100, 100, 100, 100, 100]
	g3 = [ 100, 100, 100, 32, -100, 100, 100, 92, -78, -100, 100, 100, 0, -100, -100, 100, 78, -92, -100, -100, 100, -32, -100, -100, -100]
	g4 = [ -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
	g5 = [ 100, -32, -100, -100, -100, 100, 78, -92, -100, -100, 100, 100, 0, -100, -100, 100, 100, 92, -78, -100, 100, 100, 100, 32, -100]
	g = [g0, g1, g2, g3, g4, g5]

	for i in range(height):
		for j in range(width):
			g_list = []
			r, c = i+win, j+win
			for g_idx in range(6):
				temp = 0
				for idx in range(25):
					temp += padded_img[r + kernel[idx][0]][c + kernel[idx][1]] * g[g_idx][idx]
				g_list.append(temp)
			
			if max(g_list) >= threshold:
				new_img[i][j] = 0
			else:
				new_img[i][j] = 255
	return new_img



def main():
	
	lena = io.imread('lena.bmp')
	io.imsave("roberts.png", Roberts(lena, 12))
	io.imsave("prewitt.png", Prewitt(lena, 24))
	io.imsave("sobel.png", Sobel(lena, 38))
	io.imsave("frei_and_chen.png", Frei_and_Chen(lena, 30))
	io.imsave("kirsch.png", Kirsch(lena, 135))
	io.imsave("robinson.png", Robinson(lena, 43))
	io.imsave("nevatia_babu.png", Nevatia_Babu(lena, 12500))
	
if __name__ == '__main__':
	main()
