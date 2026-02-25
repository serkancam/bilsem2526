import cv2
import os
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","soccer-in-green.jpg")

resim_o=cv2.imread(yol)
yuk,gen,kanal=resim_o.shape
oteleme_matrisi=np.float32([[1,0,100],[0,1,0]])

otelenmis=cv2.warpAffine(resim_o,oteleme_matrisi,(gen,yuk))

cv2.imshow("orijinal",resim_o)
cv2.imshow("otelenmis",otelenmis)
cv2.waitKey(0)
cv2.destroyAllWindows()