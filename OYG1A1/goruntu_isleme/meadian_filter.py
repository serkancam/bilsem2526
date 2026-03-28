import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","salt-pepper.jpg")

img=cv2.imread(yol)
img_median55=cv2.medianBlur(img,5)



#gösterim
cv2.imshow("orijinal",img)
cv2.imshow("img_median55",img_median55)
cv2.waitKey(0)
cv2.destroyAllWindows()