import cv2
import os 
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","salt-pepper.jpg")

img=cv2.imread(yol)

img_median=cv2.medianBlur(img,5)

#görsterimler

cv2.imshow("orijinal",img)
cv2.imshow("median_filter",img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()