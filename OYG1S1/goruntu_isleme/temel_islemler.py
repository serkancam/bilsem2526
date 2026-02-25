import cv2
import numpy
import os


# print(os.getcwd())
# "/home/serkan/Belgeler/bilsem2526/OYG1S1/goruntu_isleme"
# "/home/serkan/Belgeler/bilsem2526/OYG1S1"
yol="./goruntu_isleme/bolum1/marsrover.png"#path-yol

resim=cv2.imread(yol)
xsol=125
xsag=155
yust=255
yalt=290
print(resim)
parca1=resim[yust:yalt,xsol:xsag]
resim_kopya=resim.copy()
# resim_kopya[yust:yalt,xsol:xsag]=[0,0,255]

resim_kopya[:,:,0]=0
resim_kopya[:,:,2]=0

cv2.imshow("pencere",resim)
cv2.imshow("parca",parca1)
cv2.imshow("kopya",resim_kopya)
cv2.waitKey(0)