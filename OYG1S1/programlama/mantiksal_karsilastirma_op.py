# mantiksal_karsilastirma_op.py

# girilen fiyat 10000 birimden küçükse True, küçük değilse False üreten kodu yazalım


fiyat=float(input("fiyat giriniz:"))#float("300")-->300.0
sonuc= fiyat<10000
print(f"{fiyat} < 10000 --> {sonuc}")

#ram miktarı 6 GB den fazla olsun 
#yani ram 6GB veya daha büyükse True, değilse False
ram_miktari=int(input("RAM miktarını giriniz:"))
ram_sonuc=ram_miktari >= 6
print(f"{ram_miktari}>=6 --> {sonuc}")

#fiyatı 5000-10_000 arası, ram boyutu 6 GB büyük(6GB dahil), Kamerası 48MP(48 MBdahil) büyük telefonlar için True, diğer durumlar için false çıkan kodu yazalım.
kamera_mp=float(input("kamera çözünürlüğü"))

alma_durumu = (fiyat >= 5000 and fiyat <= 10000) and (ram_miktari >= 6 ) and(kamera_mp >= 48)


