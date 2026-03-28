import cv2
import numpy as np
import os

resim=np.zeros((600,800,3),dtype=np.uint8)

cv2.line(resim,(0,0),(799,599),(255,0,0),2)
cv2.line(resim,(799,0),(0,599),(0,255,255),5)
cv2.rectangle(resim,(10,280),(110,320),(255,255,0),1)
cv2.rectangle(resim,(689,280),(789,320),(255,0,255),-1)
cv2.circle(resim,(399,529),50,(220,2,78),0)
cv2.circle(resim,(399,69),50,(220,2,78),0)

points=np.array([[150,50],[110,100],[190,100]],dtype=np.int32)
cv2.polylines(resim,[points],True,(15,100,200),1)








#gösterimler
cv2.imshow("siyah",resim)
# cv2.imshow("resim2",resim2)
cv2.waitKey(0)
cv2.destroyAllWindows()