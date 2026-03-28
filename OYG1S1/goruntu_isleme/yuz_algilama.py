import cv2
import numpy as np
import os


cascade_yolu=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","haarcascade_frontalface.xml")
siniflandirici=cv2.CascadeClassifier(cascade_yolu)
kamera=cv2.VideoCapture(0)
while True:
    durum,cerceve=kamera.read()
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=siniflandirici.detectMultiScale(gri,1.1,5)       
    for yuz in yuzler:
        (x,y,w,h)=yuz
        cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),1)
      
     
    cv2.imshow("kamera",cerceve)
    if not(durum) or cv2.waitKey(5)==27:
        break


kamera.release()
cv2.destroyAllWindows()
        
