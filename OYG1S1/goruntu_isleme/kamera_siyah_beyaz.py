import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
while True:
    durum,frame=kamera.read()
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    t,siyah_beyaz=cv2.threshold(gri,180,255,cv2.THRESH_BINARY)
    t,otsu=cv2.threshold(gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    adaptif=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,3)
    median=cv2.medianBlur(frame,17)
    canny=cv2.Canny(gri,10,170)
    
    #gösterimler
    cv2.imshow("orijinal",frame)
    cv2.imshow("gri",gri)
    cv2.imshow("siyah_beyaz",siyah_beyaz)
    cv2.imshow("otsu",otsu)
    cv2.imshow("adaptif",adaptif)
    cv2.imshow("median",median)
    cv2.imshow("canny",canny)
    if not(durum) or cv2.waitKey(20)==27:
        break
    
kamera.release()
cv2.destroyAllWindows()
    
    
    
