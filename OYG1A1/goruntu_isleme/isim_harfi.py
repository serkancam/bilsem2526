import cv2 
import numpy as np

r33=[
    [200,255,256],
    [10,20,50],
    [20,200,50]
]#liste 
# opencv verileri ndarray(n dimension array) yapısında ister. Bu yapıda numpy veri türüdür.

r33_n=np.array(r33,dtype=np.uint8)

print("tipi:",r33_n.dtype)
harf=[
    [0,0,0,0,0,0,0,0],
    [0,255,255,255,255,255,255,0],
    [0,255,0,0,0,0,0,0],
    [0,255,0,0,0,0,0,0],
    [0,255,255,255,255,255,255,0],
    [0,0,0,0,0,0,255,0],
    [0,0,0,0,0,0,255,0],
    [0,255,255,255,255,255,255,0],
    [0,0,0,0,0,0,0,0]
    
    ]

harf_n=np.array(harf,dtype=np.uint8)
#gösterim
cv2.imshow("r33",r33_n)
cv2.imshow("harf",harf_n)
cv2.waitKey(0)

