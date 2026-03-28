import cv2 
import numpy as np

res1=cv2.imread("goruntu_isleme/bolum2/fark1.png")
res2=cv2.imread("goruntu_isleme/bolum2/fark2.png")

h,w,c=res2.shape

res1=res1[0:h,0:w]

diff=cv2.absdiff(res1,res2)

diff_gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(diff_gray,3)
t,bw=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
contours,hiy=cv2.findContours(bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    (x,y,w,h)=cv2.boundingRect(contour)
    area_of_contour=cv2.contourArea(contour)
    if area_of_contour>500:
        cv2.rectangle(res1,(x,y),(x+w,y+h),(0,0,255),2)
        
cv2.imshow("fark",res1)
cv2.imshow("re2",res2)
cv2.waitKey(0)
