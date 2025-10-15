# ders_gecme.py
# bir öğrenci bir dersten 2 sınav  ve bir performans notu alır.
# öğrencinin dersten geçmesiçin iki yolu vardır.
# not ortlaması 50 den büyük veya 50 ye eşit olacak
#veya
#2. sınav notu 70 veya 70 ten büyük olacak.
# 3 notun değerini(s1,s2,pn) alarak öğrenci dersten geçti ise True, geçemedi ise False değerini bir değişkene aktaran python kodunu yazınız.
#notlar float olmalıdır.

s1=float(input("sınav1 notu:"))
s2=float(input("sınav2 notu:"))
pn=float(input("performans notu:"))

ortalama=(s1+s2+pn)/3

sonuc=(ortalama>=50) or (s2>=70)
print(f"sonuc={sonuc},ortalama={ortalama}")

if (ortalama>=50) or (s2>=70):
    print("dersi geçtiniz.")
    print("Tebrik ederiz.")
else:
    print("dersten kaldınız.")
    print("üzgünüz.")