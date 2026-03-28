import cv2
import numpy as np
from datetime import datetime as dt

kamera=cv2.VideoCapture(0)
durum1,eski=kamera.read()
durum2,yeni=kamera.read()

while True:
    fark=cv2.absdiff(yeni,eski)
    fark_blur=cv2.medianBlur(fark,5,0)
    fark_gri=cv2.cvtColor(fark_blur,cv2.COLOR_BGR2GRAY)
    t,sb=cv2.threshold(fark_gri,20,255,cv2.THRESH_BINARY)
    konturlar,h=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for kontur in konturlar:
        x,y,w,h=cv2.boundingRect(kontur)
        kontur_alani=cv2.contourArea(kontur)
        if kontur_alani>1000:
            cv2.rectangle(eski,(x,y),(x+w,y+h),(0,255,0),1)
            metin="hareket algilandi..."
            cv2.putText(eski,metin,(20,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)        
    cv2.imshow("fark",fark)
    cv2.imshow("sb",sb)
    cv2.imshow("eski",eski)
    if not(durum2) or cv2.waitKey(10)==27:
        break    
    eski=yeni
    durum2,yeni=kamera.read()
kamera.release()
cv2.destroyAllWindows()