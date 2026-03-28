import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","nature.jpg")
img=cv2.imread(yol)
img_gauss55=cv2.GaussianBlur(img,(5,5),0)

#gösterimler
cv2.imshow("orijinal",img)
cv2.imshow("img_gauss55",img_gauss55)

cv2.waitKey(0)
cv2.destroyAllWindows()