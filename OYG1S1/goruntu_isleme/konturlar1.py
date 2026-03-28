import cv2
import os
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","rice_1.jpg")
#1- resmi oku
img=cv2.imread(yol)
#2- filtre(gauss,mean,median,bilaterel)
blur=cv2.medianBlur(img,7,0)
#3- gri tonlama
gri=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
#4- dinamik eşikleme
adaptif=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,3)
#5- kontur tespit
kontular1,hiyerarsi1=cv2.findContours(adaptif,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#6- konturları çizdir
kopya1=img.copy()
kopya2=img.copy()
cv2.drawContours(kopya1,kontular1,-1,(0,255,0),1)


##4. adımlar tek hamlede  canny adımı ile yapılabilir.
canny=cv2.Canny(gri,100,170)
#5-kontur
kontular2,hiyerarsi2=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#6- konturları çizdir
cv2.drawContours(kopya2,kontular2,-1,(0,255,0),1)

#gösterimler
cv2.imshow("img",img)
cv2.imshow("adaptif",adaptif)
cv2.imshow("canny",canny)
cv2.imshow("kopya1",kopya1)
cv2.imshow("kopya2",kopya2)
#resmi kaydetme(current working directory)
kayit_yolu=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","rice_1_sonuc.jpg")
cv2.imwrite(kayit_yolu,kopya2)

cv2.waitKey(0)
cv2.destroyAllWindows()