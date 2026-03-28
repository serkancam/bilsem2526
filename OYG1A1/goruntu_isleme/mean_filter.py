import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","nature.jpg")
img=cv2.imread(yol)


img_mean55=cv2.blur(img,(5,5))
img_median55=cv2.medianBlur(img,5)


cv2.imshow("orijinal",img)
cv2.imshow("img_mean55",img_mean55)
cv2.imshow("img_median55",img_median55)
cv2.waitKey(0)
cv2.destroyAllWindows()
