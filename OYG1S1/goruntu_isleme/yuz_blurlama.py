import cv2
import numpy as np
import os

cascade_yolu=os.path.join(os.getcwd(),"goruntu_isleme","bolum2","haarcascade_frontalface.xml")
siniflandirici=cv2.CascadeClassifier(cascade_yolu)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler=siniflandirici.detectMultiScale(gri,1.1,5)
    #yuzler verisi her tespit ettiği yüzün x,y,w,h verisini taşır
    for yuz in yuzler:
        x,y,w,h=yuz
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        parca=frame[y:y+h,x:x+w]
        parca_blur=cv2.blur(parca,(33,33))
        frame[y:y+h,x:x+w]=parca_blur
    cv2.imshow("sonuc",frame)
    
    if (not ret) or cv2.waitKey(50)==27:
        break
cap.release()
cv2.destroyAllWindows()
    