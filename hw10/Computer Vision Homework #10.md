# Computer Vision Homework #10

###### 資工四 b05902115 陳建丞

#### Original

<img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/lena.bmp' style='zoom:70%'>

#### Result

| Laplacian1 (Threshold = 15)                                  | Laplacian2 (Threshold = 15)                                  | Min-Variance Laplacian (Threshold = 38)                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW10_ver1/laplacian_1.png' style='zoom:100%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW10_ver1/laplacian_2.png' style='zoom:100%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW10_ver1/min_laplacian.png' style='zoom:100%'> |

| Laplacian of Gaussian (Threshold = 3000)                     | Difference of Gaussian (Threshold = 1)                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/frei_and_chen.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/kirsch.png' style='zoom:50%'> |



#### Implementation

* **Border Padding**

  * To handle the border condition, I write a function ```Border_padding(img, size)``` to return a padded version of the input image. The padding method is the same as ![Screen Shot 2019-12-09 at 11.18.38 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.18.38 PM.png) The padding size depends on the filter size of different operators.

* **Edge Dectection Operator**

  All the operators follow the same processing steps

  1. Create corresponding filter (Laplacian、Minimum-Variance Laplacian、LOG、DOG)
  2. Border padding according to filter size
  3. Convolutionally traverse through each pixel
  4. Compute gradient magnitude
  5. Compare the result with threshold and -threshold.
     * If gradient magnitude $\geq$ threshold, mark as 1
     * If gradient magnitude $\leq$ -threshold, mark as -1
     * else, mark as 0
  6. Store the marked result to a marked image.
  7. Traverse through the marked image to apply zero crossing.
  8. If a pixel's marked value is 1 and any of its 8 neighbors is -1. $\Rightarrow$ edge pixel

* **Laplacian**

  ![Screen Shot 2019-12-14 at 3.28.53 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-14 at 3.28.53 PM.png)

* **Minimum-Variance Laplacian**

  ![Screen Shot 2019-12-14 at 3.29.01 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-14 at 3.29.01 PM.png)

* **Laplacian of Gaussian**

  ![Screen Shot 2019-12-14 at 3.29.09 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-14 at 3.29.09 PM.png)

* **Difference of Gaussian**

  ![Screen Shot 2019-12-14 at 3.29.17 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-14 at 3.29.17 PM.png)

#### Code Segment

* Border Padding

  ``````python
  def Border_padding(img, size)	
  	
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
  ``````

  

* Zero Crossing

  ``````python
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
  ``````

  