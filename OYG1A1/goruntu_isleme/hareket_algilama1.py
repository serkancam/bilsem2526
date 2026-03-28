import cv2
import numpy as np

cap=cv2.VideoCapture(0)#capture

if not cap.isOpened():
    print("hata stream yok")
    exit()
gen=int(cap.get(3))#
yuk=int(cap.get(4))#

state1,old=cap.read()
state2,new=cap.read()

while True:
    i+=1
    #state,frame=cap.read()
    diff=cv2.absdiff(new,old)
    diff_gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.medianBlur(diff_gray,3)
    t,bw=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    contours,hiy=cv2.findContours(bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        area_of_contour=cv2.contourArea(contour)
        if area_of_contour>1000:
            cv2.rectangle(old,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(old,"hareket algilandi",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
        
    cv2.imshow("fark",diff)
    cv2.imshow("gray",diff_gray)
    cv2.imshow("blur",blur)
    cv2.imshow("bw",bw)
    cv2.imshow("old",old)
    if not(state2) or cv2.waitKey(20)==27:
        break
    
    old=new
    state2,new=cap.read()

cap.release()
cv2.destroyAllWindows()
    
    