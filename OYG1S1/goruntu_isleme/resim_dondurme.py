import cv2
import numpy as np
import os

img_path = os.path.join(os.getcwd(), "goruntu_isleme", "bolum2", "zebrasmall.png")
img = cv2.imread(img_path)
# resim dosyasını döndürmek için çeşirli değerleri bulmamız ve bu değeler ile dönme matrisi oluşturmamız gerekirr
h, w, c = img.shape
# dönüşüm matiris için dönme açısı, dönme merkez ve dönerken hangi ölçekle dönecek
merkez = (w//2, h//2)
olcek = 1.0
aci = 45
carpan = 0.98
# cv2.imshow("orjinal",img)
while True:
    # dönüşüm matrisi
    donusum_matrisi = cv2.getRotationMatrix2D(merkez, aci%360, olcek)
    donmus_resim = cv2.warpAffine(img, donusum_matrisi, (w, h))
    cv2.imshow("donmus", donmus_resim)
    aci += 5
    if olcek < 0.05:
        carpan = 1.02
    elif olcek > 1.0:
        carpan = 0.98
    olcek *= carpan
    if cv2.waitKey(25)==27:
        break
cv2.destroyAllWindows()