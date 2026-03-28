import cv2 
import numpy as np
import os

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","rice_1.jpg")
#0- resim oku
img=cv2.imread(yol)
#1- filtre
filtreli=cv2.medianBlur(img,7)
#2- gri tonlama(gray scale)
gri=cv2.cvtColor(filtreli,cv2.COLOR_BGR2GRAY)
#3- siyah beyaz eşikleme(binarization)-adaptif threshold
adaptif=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
#4- konturları bul
konturlar,h=cv2.findContours(adaptif,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#5- konturları çizdir
kopya1=img.copy()
cv2.drawContours(kopya1,konturlar,-1,(0,255,0),1)
###################canny edge detection###############
#3v2
canny=cv2.Canny(gri,100,170)
#4v2
konturlarC,hc=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#5v2 konturları çizdir
kopya2=img.copy()
cv2.drawContours(kopya2,konturlarC,-1,(0,255,0),1)

kayit_yolu=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","rice_1_sonuc.jpg")
cv2.imwrite(kayit_yolu,kopya2)
#gösterimler

cv2.imshow("orijinal",img)
cv2.imshow("gri",gri)
cv2.imshow("adaptif",adaptif)
cv2.imshow("kopya1",kopya1)
cv2.imshow("kopya2",kopya2)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
