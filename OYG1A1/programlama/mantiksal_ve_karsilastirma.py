# mantiksal_ve_karsilastirma.py
# fiyatı 10.000 tl den düşük olsun(yani bu şart sağlanırsa True, sağlnamaz ise False)
#1-fiyat adında bir değiken oluşturup, bu değeri giriş yapılmasını sağlayını ve değeri float tipine dönüştürünüz.


fiyat=float(input("değer giriniz:"))
print(fiyat<10_000)

#fiyat 10 bine eşitse True, değilse False
print(fiyat==10000)

#fiyat değeri 5000 ile 10000 arasında ise(5000 ve 10000 dahil) True, değilse False olsun
print(fiyat>=5000 and fiyat<=10000)
ram=int(input("RAM boyutunu giriniz:"))
kamera_mp=int(input("Kamera kaç megapiksel:"))
# fiyatı 5000-10_000 arası, ram boyutu 6 GB büyük(6GB dahil), Kamerası 48MP(48 MBdahil) büyük telefonlar için True, diğer durumlar için false çıksın
sonuc=(fiyat>=5000 and fiyat<=10_000) and (ram>=6) and (kamera_mp>=48)
# fiyat>=5000 and fiyat<=10_000 and ram>=6 and kamera_mp>=48
print(f"sonuc={sonuc}")



