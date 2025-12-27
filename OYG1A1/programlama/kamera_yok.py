import cv2
try: 
    cap=cv2.VideoCapture(22)
except cv2.error as e:
    print("hata")
else:
    while True:
        ret,frame=cap.read()
        cv2.imshow("test",frame)
        if not ret or cv2.waitKey(1)=='q':
            break
    cap.release()
    
print("sssssssssssss")