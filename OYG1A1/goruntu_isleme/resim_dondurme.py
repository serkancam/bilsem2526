import cv2
import os
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","zebrasmall.png")
img=cv2.imread(yol)
#aynalama(flip)
#0--> dikey,1--> yatay,-1--> hem dikey hem yatay
img_dikey=cv2.flip(img,0)
img_yatay=cv2.flip(img,1)
img_yakey=cv2.flip(img,-1)
#rotasyon
yuk,gen,kanal=img.shape
merkez=(50,50)
aci=-45#saat yönünde
olcek=1.0
dondurme_matrisi=cv2.getRotationMatrix2D(merkez,aci,olcek)
donmus_img=cv2.warpAffine(img,dondurme_matrisi,None)

#resmi ortadan saat yönünün tersine 30 derece  döndürün
merkez2=(gen//2,yuk//2)
aci2=30#saat yönünde
olcek2=1.0
dondurme_matrisi2=cv2.getRotationMatrix2D(merkez2,aci2,olcek2)
donmus_img2=cv2.warpAffine(img,dondurme_matrisi2,None)
#gösterimler
cv2.imshow("img",img)
cv2.imshow("img_dikey",img_dikey)
cv2.imshow("img_yatay",img_yatay)
cv2.imshow("img_yakey",img_yakey)
cv2.imshow("tesdonmus_img",donmus_img)
cv2.imshow("tesdonmus_img2",donmus_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()