import cv2
import numpy as np

classifier=cv2.CascadeClassifier("./goruntu_isleme/bolum2/haarcascade_frontalface.xml")
cap=cv2.VideoCapture(0)
while True:
    durum,cerceve=cap.read()
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=classifier.detectMultiScale(gri,1.1,9)
    for (x,y,w,h) in yuzler:      
        yuz=cerceve[y:y+h,x:x+w]
        blur=cv2.medianBlur(yuz,99)
        cerceve[y:y+h,x:x+w]=blur     
    cv2.imshow("sonuc",cerceve)
    if not(durum) or cv2.waitKey(50)==27:
        break
cap.release()
cv2.destroyAllWindows()
