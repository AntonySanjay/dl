# -*- coding: utf-8 -*-
"""image_contours.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h-SM2PRDW8PBssBzIHTQVrmWf49W0iiH
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/content/download.jfif')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred=cv2.GaussianBlur(gray,(11,11),0)

edged=cv2.Canny(blurred, 30,150)

cnts,_= cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

coins = image.copy()

cv2.drawContours(coins,cnts,-1,(0,255,0),3)

plt.imshow(coins)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

plt.imshow(edged)