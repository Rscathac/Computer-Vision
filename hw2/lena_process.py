from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2

lena = io.imread('lena.bmp')

# Binarize image
lena_binarized = lena.copy()

for i in range(len(lena_binarized)):
	for j in range(len(lena_binarized)):
		if lena_binarized[i][j] >= 128:
			lena_binarized[i][j] = 255
		else:
			lena_binarized[i][j] = 0

#io.imsave('lena_binarized.png', lena_binarized)


# Histogram
pixels = np.zeros((256), dtype = int)

for row in lena:
	for i in row:
		pixels[i] += 1

plt.bar(range(len(pixels)), pixels)
plt.title('Histogram of Lena.bmp')
plt.xlabel('Gray scale value')
plt.ylabel('Frequency')
#plt.show()
plt.savefig('histogram.png', dpi=130)


# Connected component labeling
pixels = lena_binarized.copy()
labels = []
pixels_label = [[-1] * len(lena_binarized) for h in range(len(lena_binarized))]

for i in range(len(lena_binarized)):
	for j in range(len(lena_binarized)):
		if pixels[i][j] == 0:
			continue

		left_label = -1
		if j > 0 and pixels_label[i][j-1] != -1:
			left_label = pixels_label[i][j-1]
		if i > 0 and pixels_label[i-1][j] != -1:
			top_label = pixels_label[i-1][j]

			if left_label != -1 and left_label != top_label:
				for x, y in labels[left_label]:
					pixels_label[x][y] = top_label
				labels[top_label] += labels[left_label]
				labels[left_label] = []

			left_label = top_label
		
		if left_label == -1:
			left_label = len(labels)
			labels.append([(i, j)])
		else:
			labels[left_label].append((i, j))

		pixels_label[i][j] = left_label

lena_connected = cv2.cvtColor(lena_binarized, cv2.COLOR_GRAY2RGB)

new_labels = []

for label in labels:
	if len(label) >= 500:
		new_labels.append(label)


for component in new_labels:
	
	(left, top), (right, bottom) = component[0], component[0]
	cx, cy = 0, 0
	for y, x in component:
		if x < left:
			left = x
		if x > right:
			right = x
		if y < top:
			top = y
		if y > bottom:
			bottom = y

		cx += x
		cy += y

	cx = round(cx / len(component))
	cy = round(cy / len(component))


	cv2.rectangle(lena_connected, (left, top), (right, bottom), (255, 0, 0), 1)
	cv2.line(lena_connected, (cx-10, cy), (cx+10, cy), (255, 0, 0), 5)
	cv2.line(lena_connected, (cx, cy-10), (cx, cy+10), (255, 0, 0), 5)


io.imshow(lena_connected)
#io.imsave('lena_connected.png', lena_connected)
