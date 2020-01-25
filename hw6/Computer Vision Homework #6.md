# Computer Vision Homework #6

###### 資工四 b05902115 陳建丞

### 1. Downsampling

* **Result (400%)** 

  <img src = "/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW6_ver1/lena_down.png" style="zoom:400%"/>

  

* **Implementation**

  Create a new image with size 64x64. Then use the 8x8 blocks of original image to  take the topmost-left pixel as the downsampled new image.
  
``````python
  def Downsampling(img, size):
	
  	img_down = np.zeros((int(img.shape[0]/size), int(img.shape[1]/size)), dtype = int)
  	
  	for i in range(img_down.shape[0]):
  		for j in range(img_down.shape[1]):
  			img_down[i][j] = img[i*size][j*size]
  	
  	return img_down
  ``````
  


### 2.  Yokoi

* **Result**

  ![Screen Shot 2019-11-17 at 9.08.26 PM](/Users/Ingram/Desktop/Screen Shot 2019-11-17 at 9.08.26 PM.png)

  

  

* **Implementation**
$$
  \begin{equation}
    h(b,c,d,e) =
    \begin{cases}
        q & \text{if b = c and (d $\neq$ b $\or$ e $\neq$ b)}\\
      r & \text{if b = c and (d = b $\and$ e = b)}\\
        s & \text{if b $\neq$ s}
      \end{cases}       
  \end{equation}
  $$
  
  $$
  \begin{equation}
    f(a_1,a_2,a_3,a_4) =
      \begin{cases}
        5 & \text{if $a_1$ = $a_2$ = $a_3$ = $a_4$ = r}\\
        n & \text{where n = number of \{$a_k|a_k=q$\}}\\
      \end{cases}       
  \end{equation}
  $$
  
  I follow the formula above to iterate through downsampled image. I write function ```h(b,c,d,e)``` and ```f(a_1,a_2,a_3,a_4)​```. Since it takes time to calculate $h(b,c,d,e)$ every time, I create a h table to store the h values all 16 possible $(b,c,d,e)$.
  
  ```python
  def Yokoi(img):
  	
  	yokoi = np.zeros((img.shape[0], img.shape[1]), dtype = int)
  	bin_img = img.copy()
  	bin_img[bin_img==255] = 1
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
  	for i in range(img.shape[0]):
  		for j in range(img.shape[1]):
  			
  			if bin_img[i, j] == 0:
  				continue
  
  			f_input = []
  			for k in neighbors:
    				
  				idx = (i, j) + k
  				bin_value = []
  				for m, n in idx:
  					if m < 0 or n < 0 or n >= img.shape[0] or m >= img.shape[1]:
  						bin_value.append(0)
  					else:
  						bin_value.append(bin_img[m, n])
  				
  				f_input.append(h_table[bin_value[0], bin_value[1], bin_value[2], bin_value[3]])
  			
  			yokoi[i][j] = f(f_input[0], f_input[1], f_input[2], f_input[3])
  				
  	return yokoi
  ```
  
  

* **Python package**
  * **skimage** : read and write image
  * **numpy** : array manipulation
  
* **Other function**

  ```Binarize(img, threshold)``` : To generate a binary image (from previous homework)

  ```h(b,c,d,e)```：Return the corresponding h value.

  ```f(a_1, a_2, a_3, a_4)```：Return the corresponding f value.