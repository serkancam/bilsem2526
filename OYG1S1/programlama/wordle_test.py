import time
import os
import random
dosya_yolu="/home/serkan/Belgeler/bilsem2526/OYG1S1/programlama/wordle.txt"
baglanti=open(dosya_yolu,mode="r",encoding="utf-8")
okunan=baglanti.read()
baglanti.close()

soru=random.choice(okunan.split(",")).lower().strip()
hak=1
while  hak<=5:
    os.system("clear")
    kelime=input("kelime gir:")
    uzunluk=len(kelime)
    i=0
    
    while i<uzunluk:
       
        if kelime[i]==soru[i]:
            print(kelime[i].upper(),end=" ")
        elif kelime[i] in soru:
            print(kelime[i].lower(),end=" ")
        else:
            print("_",end=" ")
        i=i+1
        # print(i)
        time.sleep(2)
    hak+=1
    