# Computer Vision Homework #9

###### 資工四 b05902115 陳建丞

#### Original

<img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/lena.bmp' style='zoom:70%'>

#### Result

| Roberts (Threshold = 12)                                     | Prewitt (Threshold = 24)                                     | Sobel (Threshold = 38)                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/roberts.png' style='zoom:100%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/prewitt.png' style='zoom:100%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/sobel.png' style='zoom:100%'> |

| Frei and Chen (Threshold = 30)                               | Kirsch (Threshold = 135)                                     | Robinson (Threshold = 43)                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/frei_and_chen.png' style='zoom:100%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/kirsch.png' style='zoom:100%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/robinson.png' style='zoom:100%'> |

| Nevatia Babu (Threshold = 12500)                             |
| ------------------------------------------------------------ |
| <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW9_ver1/nevatia_babu.png' style='zoom:46%'> |



#### Implementation

* **Border Padding**

  * To handle the border condition, I write a function ```Border_padding(img, size)``` to return a padded version of the input image. The padding method is the same as ![Screen Shot 2019-12-09 at 11.18.38 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.18.38 PM.png) The padding size depends on the filter size of different operators.

* **Edge Dectection Operator**

  All the operators follow the same processing steps

  1. Create corresponding filter
  2. Border padding according to filter size
  3. Convolutionally traverse through each pixel
  4. Compute gradient magnitude or select the maximun value
  5. Compare the result with threshold and write the value to a new image

* **Roberts**

  ![Screen Shot 2019-12-09 at 11.53.48 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.53.48 PM.png)

* **Prewitt**

  ![Screen Shot 2019-12-09 at 11.54.21 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.54.21 PM.png)

* **Sobel**

  ![Screen Shot 2019-12-09 at 11.54.39 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.54.39 PM.png)

* **Frei and Chen**

  ![Screen Shot 2019-12-09 at 11.55.14 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.55.14 PM.png)

* **Kirsch**

  ![Screen Shot 2019-12-09 at 11.55.32 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.55.32 PM.png)

* **Robinson**

  ![Screen Shot 2019-12-09 at 11.55.55 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.55.55 PM.png)

* **Nevatia Babu**

  ![Screen Shot 2019-12-09 at 11.56.14 PM](/Users/Ingram/Desktop/Screen Shot 2019-12-09 at 11.56.14 PM.png)

