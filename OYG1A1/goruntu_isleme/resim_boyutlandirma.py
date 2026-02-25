import cv2
import os
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","zebra.png")
img=cv2.imread(yol)

yuk,gen,kanal=img.shape

#yol1 fx,fy

kucuk1=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
#*yol2 hedef boyut belirlemek
kucuk2=cv2.resize(img,(100,200),interpolation=cv2.INTER_AREA)
#yol3 en/boy oranı korunarak
oran=gen/yuk
yeni_gen=100
yeni_yuk=int(yeni_gen/oran)

kucuk3=cv2.resize(img,(yeni_gen,yeni_yuk),interpolation=cv2.INTER_AREA)
#soccer-in-green.jpg resminin yüksekliğini 500 yapınız. Yeni genişliği gen/yuk oranını koruyarak hesaplayınız. 



###gösterimler###
cv2.imshow("kucuk1",kucuk1)
cv2.imshow("kucuk2",kucuk2)
cv2.imshow("kucuk3",kucuk3)

cv2.imshow("orijinal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()