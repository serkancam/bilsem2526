import os
import random
import time

#dosyadan verileri oku
adres="/home/serkan/Belgeler/bilsem2526/OYG1A1/programlama/sorular.txt"
baglanti=open(adres,mode="r",encoding="utf-8")
okunan=baglanti.read()
baglanti.close()
# print(okunan)
sorular=okunan.split(",")

# print(soru)

# os.system("clear")
# for _ in soru:
#     print("_",end=" ")
def adam_ciz(hk):
    ADAM_ASMACA = [
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
    
    
def soru_ciz(s,liste):
    cizilen_soru=""
    for h in s:
        if h in liste:
            cizilen_soru+=h+" "
        else:
            cizilen_soru+="_ "
    print(cizilen_soru)
    if not("_" in cizilen_soru):
        print("Tebrikler doğru bildiniz")
        return -1
# print()
def oyun():
    soru=random.choice(sorular).strip().lower()
    s_harfler=[]
    hak=1
    while hak<=6:
        os.system("clear")
        adam_ciz(hak-1)
        gelen=soru_ciz(soru,s_harfler)
        if gelen==-1:
            return 0
        harf=input(f"({7-hak})-Bir harf giriniz:").lower()
        if len(harf)!=1 or (not harf.isalpha()) or (harf in s_harfler):
            print("lütfen söylenmeyen bir harf giriniz:")
            time.sleep(1)
            continue
        s_harfler.append(harf)
        if not(harf in soru):
            hak+=1
    os.system("clear")
    adam_ciz(hak-1)
    print("cevap:",soru)

while(True):
    os.system("clear")
    durum=input("oynamak için o, çıkmak için x tuşuna basığp entera basınız:").lower()
    if durum=="o":
        oyun()
        time.sleep(5)
    else:
        break


