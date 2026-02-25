import cv2
import os
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","soccer-in-green.jpg")
img=cv2.imread(yol)

#oteleme matrisi
oteleme_matrisi=np.float32([[1,0,50],[0,1,20]])
otelenmis_resim=cv2.warpAffine(img,oteleme_matrisi,None)




#gösterimler
cv2.imshow("img",img)
cv2.imshow("otelenmis_resim",otelenmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()