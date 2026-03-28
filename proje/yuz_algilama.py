import cv2
import numpy as np

classifier=cv2.CascadeClassifier("./resource/haarcascade_frontalface.xml")
cap=cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read()
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=classifier.detectMultiScale(gri,1.1,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),2)
        
    
    cv2.imshow("sonuc",cerceve)
    
    
    if not(durum) or cv2.waitKey(50)==27:
        break
    
cap.release()
cv2.destroyAllWindows()
