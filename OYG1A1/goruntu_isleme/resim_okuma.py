import cv2
import numpy as np
import os


#/home/serkan/Belgeler/bilsem2526/OYG1A1/goruntu_isleme/bolum1/marsrover.png
kok_dizin=os.getcwd()
resim_yolu=os.path.join(kok_dizin,"goruntu_isleme","bolum1","marsrover.png")
print(resim_yolu)
resim=cv2.imread(resim_yolu)

# print(resim)
print(resim.shape)#bu resmmin önemli bilgilerini verir
yukseklik,genislik,kanal=resim.shape

parca1=resim[158:175,195:225]

#sadece kırmızı tonlar
resim_kirmizi=resim.copy()
resim_kirmizi[::,::,0]=0 #blue kanalı sıfırlandı
resim_kirmizi[::,::,1]=0 #green kanalı sıfırlandı


#göster
cv2.imshow("pencere1",resim)
cv2.imshow("p1",parca1)
cv2.imshow("red",resim_kirmizi)

cv2.waitKey(0)
