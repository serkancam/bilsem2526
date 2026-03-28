import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","scanned_doc.png")
#0- resmi oku
img=cv2.imread(yol)
#1- median filter
filtreli=cv2.medianBlur(img,3)
#2- gri tonlamalı
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#3a- eşikleme
t,siyah_beyaz=cv2.threshold(gri,80,255,cv2.THRESH_BINARY)
#3b- farklı eşikleme işlemi(otsu eşikleme)
t,otsu=cv2.threshold(gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#3c- eşikleme ama ters renkler ile
t,siyah_beyaz_inverse=cv2.threshold(gri,80,255,cv2.THRESH_BINARY_INV)
#3d- dinamik eşikleme-adaptif threshold
adaptif=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,3)


#görüntü işleme
cv2.imshow("img",img)
cv2.imshow("filtreli",filtreli)
cv2.imshow("gri",gri)
cv2.imshow("siyah_beyaz",siyah_beyaz)
cv2.imshow("otsu",otsu)
cv2.imshow("siyah_beyaz_inverse",siyah_beyaz_inverse)
cv2.imshow("adaptif",adaptif)

cv2.waitKey(0)
cv2.destroyAllWindows()