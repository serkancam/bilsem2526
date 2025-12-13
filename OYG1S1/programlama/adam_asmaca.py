import time
import random
import os

dosya_yolu="/home/serkan/Belgeler/bilsem2526/OYG1S1/programlama/sorular.txt"
baglanti=open(dosya_yolu,mode="r",encoding="utf-8")
okunan=baglanti.read()
baglanti.close()
# print(okunan)
sorular=okunan.split(",")
# print(sorular)
soru=random.choice(sorular).lower().strip()
# print(soru)
# os.system("clear")

# for h in soru:
#     print("_ ",end="")
# print()
def adam_ciz(hk):
    ADAM_ASMACA = [
    r"""
  +---+
      |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
    print(ADAM_ASMACA[hk])
def soru_ciz(sy,hk,sr):
    os.system("clear")
    adam_ciz(hk-1)
    cizim=""
    for harf in sr:
        if harf in sy:
            cizim=cizim+harf+" "
        else:
            cizim=cizim+"_ "
    print(cizim)
    if not("_" in cizim):
        print("Tebirkler...")
        exit()
            
hak=1
soylenenler=[]
while hak<=7:
    soru_ciz(soylenenler,hak,soru)
    harf=input(f"({8-hak})harf söyle:")
    if len(harf)!=1 or (harf in soylenenler) or not (harf.isalpha()):
        print("lütfen söylenmeyen bir harf giriniz:")
        time.sleep(3)
        continue
    soylenenler.append(harf)
    if not(harf in soru):
        hak=hak+1

os.system("clear")
adam_ciz(7)
print("Kaybettiniz!!!")