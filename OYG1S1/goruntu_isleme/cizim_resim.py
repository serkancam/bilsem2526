import cv2
import numpy as np
import os

resim=np.zeros((400,300,3),dtype=np.uint8)

cv2.line(resim,(0,0),(299,399),(255,0,0),2)
cv2.line(resim,(0,399),(299,0),(0,0,255),2)
cv2.rectangle(resim,(10,189),(60,219),(0,255,0),1)
cv2.rectangle(resim,(239,189),(289,219),(0,255,255),-1)
cv2.circle(resim,(150,200),20,(255,120,30),-1)

points=np.array([[150,50],[110,100],[190,100]],dtype=np.int32)

cv2.polylines(resim,[points],True,(15,100,200),2)
cv2.imshow("orijinal",resim)

cv2.waitKey(0)