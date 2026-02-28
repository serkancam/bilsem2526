import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","sudoku.jpg")
yol2=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","salt-pepper.jpg")
img=cv2.imread(yol)
img2=cv2.imread(yol2)

img_gauss=cv2.GaussianBlur(img,(15,15),0)
beyin_gauss=cv2.GaussianBlur(img2,(5,5),0)

#gösterimler
cv2.imshow("orijinal",img)
cv2.imshow("img_gauss",img_gauss)
cv2.imshow("beyin_gauss",beyin_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()