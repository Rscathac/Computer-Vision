# Computer Vision Homework #8

###### 資工四 b05902115 陳建丞

1. **Gaussian noise with amplitude of 10**

   * Original

     <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/lena_gau10.png' style='zoom:50%'>

   * Filtered

     | 3x3 Box filter                                               | 5x5 Box filter                                               |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter3X3_on_gau10.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter5X5_on_gau10.png' style='zoom:50%'> |
     | $SNR= 17.738$                                                | $SNR=14.866$                                                 |

     | 3x3 Median filter                                            | 5x5 Median filter                                            |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter3X3_on_gau10.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter5X5_on_gau10.png' style='zoom:50%'> |
     | $SNR=17.683$                                                 | $SNR=16.006$                                                 |

     | Opening then closing                                         | Closing then opening                                         |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/opening_then_closing_on_gau10.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/closing_then_opening_on_gau10.png' style='zoom:50%'> |
     | $SNR=13.242$                                                 | $SNR=13.567$                                                 |

     

2. **Gaussian noise with amplitude of 30**

   * Original

     <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/lena_gau30.png' style='zoom:50%'>

   * Filtered

     | 3x3 Box filter                                               | 5x5 Box filter                                               |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter3X3_on_gau30.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter5X5_on_gau30.png' style='zoom:50%'> |
     | $SNR= 9.789$                                                 | $SNR=10.809$                                                 |

     | 3x3 Median filter                                            | 5x5 Median filter                                            |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter3X3_on_gau30.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter5X5_on_gau30.png' style='zoom:50%'> |
     | $SNR=10.721$                                                 | $SNR=12.438$                                                 |

     | Opening then closing                                         | Closing then opening                                         |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/opening_then_closing_on_gau30.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/closing_then_opening_on_gau30.png' style='zoom:50%'> |
     | $SNR=7.676$                                                  | $SNR=8.005$                                                  |

     

3. **Salt-and-pepper noise with probability 0.05**

   * Original

     <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/lena_sp005.png' style='zoom:50%'>

   * Filtered

     | 3x3 Box filter                                               | 5x5 Box filter                                               |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter3X3_on_sp005.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter5X5_on_sp005.png' style='zoom:50%'> |
     | $SNR= 9.453$                                                 | $SNR=11.149$                                                 |

     | 3x3 Median filter                                            | 5x5 Median filter                                            |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter3X3_on_sp005.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter5X5_on_sp005.png' style='zoom:50%'> |
     | $SNR=19.028$                                                 | $SNR=16.404$                                                 |

     | Opening then closing                                         | Closing then opening                                         |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/opening_then_closing_on_sp005.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/closing_then_opening_on_sp005.png' style='zoom:50%'> |
     | $SNR=5.988$                                                  | $SNR=5.438$                                                  |

     

4. **Salt-and-pepper noise with probability 0.1**

   * Original

     <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/lena_sp01.png' style='zoom:50%'>

   * Filtered

     | 3x3 Box filter                                               | 5x5 Box filter                                               |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter3X3_on_sp01.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/box_filter5X5_on_sp01.png' style='zoom:50%'> |
     | $SNR= 6.288$                                                 | $SNR=8.457$                                                  |

     | 3x3 Median filter                                            | 5x5 Median filter                                            |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter3X3_on_sp01.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/med_filter5X5_on_sp01.png' style='zoom:50%'> |
     | $SNR=14.787$                                                 | $SNR=15.721$                                                 |

     | Opening then closing                                         | Closing then opening                                         |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/opening_then_closing_on_sp01.png' style='zoom:50%'> | <img src='/Users/Ingram/Desktop/CSIE/4-1/Computer Vision/hw/B05902115_HW8_ver1/closing_then_opening_on_sp01.png' style='zoom:50%'> |
     | $SNR=-2.344$                                                 | $SNR=-2.541$                                                 |

