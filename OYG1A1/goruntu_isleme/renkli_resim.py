import cv2
import numpy as np

rl=[
    
    [[255,0,0],[0,0,255],[0,255,0],[200,50,30],[3,15,240]],
    
    [[255,150,0],[50,0,255],[0,255,200],[200,50,30],[3,15,240]],
    [[255,20,0],[0,0,255],[0,255,0],[200,50,30],[3,15,240]],
    [[255,0,0],[175,0,255],[0,255,0],[200,50,30],[3,15,240]],
    [[255,90,0],[90,0,255],[0,255,0],[200,50,30],[3,15,240]]
]

resim=np.array(rl,dtype=np.uint8)
r_resim=np.random.randint(0,255,(300,300,3))
r_resim=r_resim.astype(np.uint8)
cv2.imshow("resim",resim)
cv2.imshow("resim2",r_resim)
tus=cv2.waitKey(0)
print(tus)