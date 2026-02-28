import cv2 
import os
import numpy as np

yol=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","scanned_doc.png")
img=cv2.imread(yol)

#1- gri tonlamalıya dönüştürme
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape,img_gray.shape,sep="\n")
#eşikleme(thresholding) ile siyah beyaz dönüşüm(binarization)
esik,img_sb=cv2.threshold(img_gray,20,255,cv2.THRESH_BINARY)
esik,img_sb_inv=cv2.threshold(img_gray,20,255,cv2.THRESH_BINARY_INV)

# for i in range(img_gray.shape[0]):
#     for j in range(img_gray.shape[1]):
#         if img_sb[i,j]<100:
#             img_sb[i,j]=255
#         else:
#             img_sb[i,j]=0

#gösterimler

cv2.imshow("orijinal",img)
cv2.imshow("img_gray",img_gray)
cv2.imshow("img_sb",img_sb)
cv2.imshow("img_sb_inv",img_sb_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()