from skimage import io

# Read the original image
lena = io.imread('lena.bmp')
lena.shape

# Upside down
lena_upside_down = lena.copy()[::-1]
io.imshow(lena_upside_down)
io.imsave('lena_upside_down.png', lena_upside_down)


# Right side left
lena_right_side_left = lena.copy()
for i in range(len(lena_right_side_left)):
	lena_right_side_left[i] = lena_right_side_left[i][::-1]

io.imshow(lena_right_side_left)
io.imsave('lena_right_side_left.png', lena_right_side_left)


# Diagonally mirrored
lena_diagonally_mirrored = lena.copy()
for i in range(len(lena_diagonally_mirrored)):
	for j in range(len(lena_diagonally_mirrored)):
		lena_diagonally_mirrored[i][j] = lena_diagonally_mirrored[j][i]

io.imshow(lena_diagonally_mirrored)
io.imsave('lena_diagonally_mirrored.png', lena_diagonally_mirrored)





