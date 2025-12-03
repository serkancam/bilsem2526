import random
baglanti=open("./programlama/sehirler.txt","r",encoding="utf-8")
sehirler=baglanti.readlines()
baglanti.close()
# print(sehirler)
secilen=random.choice(sehirler).strip()
print("Seçilen şehir:",secilen)

for i in secilen:
    print("_",end=" ")



