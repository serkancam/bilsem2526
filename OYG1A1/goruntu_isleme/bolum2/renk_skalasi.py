import cv2
import numpy as np
def bos(x):
 pass
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("Ara Renkler")
cv2.createTrackbar("R", "Ara Renkler", 0, 255, bos)
cv2.createTrackbar("G", "Ara Renkler", 0, 255, bos)
cv2.createTrackbar("B", "Ara Renkler", 0, 255, bos)
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch, "Ara Renkler", 0, 1, bos)
while True:
    cv2.imshow("Ara Renkler", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    r = cv2.getTrackbarPos("R", "Ara Renkler")
    g = cv2.getTrackbarPos("G", "Ara Renkler")
    b = cv2.getTrackbarPos("B", "Ara Renkler")
    s = cv2.getTrackbarPos(switch, "Ara Renkler")
    if s == 0:
        img[:] = [0, 0, 0]
    if s == 1:
        img[:] = [b, g, r]
cv2.destroyAllWindows()