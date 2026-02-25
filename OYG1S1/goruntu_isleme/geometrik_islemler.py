# geometrik_islemler.py
import cv2
import numpy as np
import os
# /home/serkan/Belgeler/bilsem2526/OYG1S1/goruntu_isleme/bolum2/zebra.png
kok_dizin=os.getcwd()
print(kok_dizin)
yol=os.path.join(kok_dizin,"goruntu_isleme","bolum2","zebra.png")

resim=cv2.imread(yol)
########işlemler############
kucuk_1=cv2.resize(resim,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

#aspect ratio=genislik/yukseklik orani
yuk,gen,kanal=resim.shape
oran=gen/yuk
print(resim.shape)
print(oran)
yeni_gen=100
yeni_yuk=int(yeni_gen//oran)
print(type(yeni_yuk))

yeni_boyut=(yeni_yuk,yeni_gen)#tuple/demet
kucuk_2=cv2.resize(resim,yeni_boyut,interpolation=cv2.INTER_AREA)

#resmi 200*200 boyutuna getirip ekranda gösteriniz
yg2=200
yy2=200
PI=3.14
yb2=(yy2,yg2)
kucuk_3=cv2.resize(resim,yb2,interpolation=cv2.INTER_AREA)

####flip######

yty_flip=cv2.flip(kucuk_1,0)#x ekseninde flip
dky_flip=cv2.flip(kucuk_1,1)#y ekeseninde flip
yky_flip=cv2.flip(kucuk_1,-1)# x ve y ekseninde aynı anda flip

####döndürme####
h,w,c=kucuk_1.shape

orta=(h//2,w//2)
aci=45
olcek=1.0
dondurme_matrisi=cv2.getRotationMatrix2D(orta,aci,olcek)
donmus_resim=cv2.warpAffine(kucuk_1,dondurme_matrisi,(w,h))

#####sol üst noktadan saat yönünde 35 derece döndürünüz####

#######işlemler#############
cv2.imshow("res",resim)
cv2.imshow("res2",kucuk_1)
cv2.imshow("res3",kucuk_2)
cv2.imshow("res4",kucuk_3)
cv2.imshow("ytyf",yty_flip)
cv2.imshow("dkyf",dky_flip)
cv2.imshow("yky",yky_flip)
cv2.imshow("donmus1",donmus_resim)
cv2.waitKey(0)
