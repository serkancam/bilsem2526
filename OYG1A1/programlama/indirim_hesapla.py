# Bir kafede satılan ürünlerin fiyatları şöyledir: Çay (5 TL), Kahve (10 TL), Tatlı (15 TL). Kullanıcıdan kaç adet çay, kahve ve tatlı aldığını sorun. Toplam tutarı hesaplayın ve aşağıdaki indirim kurallarını uygulayarak son ödemesi gereken tutarı ekrana yazdırın:

#     Toplam tutar 50 TL veya daha fazlaysa, %10 indirim yapın.

#     Toplam tutar 100 TL veya daha fazlaysa, %20 indirim yapın.

#     Diğer durumlarda indirim uygulamayın.
cay_adet=int(input("kaç çay içtiniz:"))# 00001000  int("8")-->8, float("8")-->8.0
kahve_adet=int(input("kaç kahve içtiniz:"))
tatli_adet=int(input("kaç tatlı yediniz:"))

cay_fiyat=5
kahve_fiyat=10
tatli_fiyat=15

odenecek= (cay_adet*cay_fiyat)+(kahve_adet*kahve_fiyat)+(tatli_adet*tatli_fiyat)

if odenecek>=100:#odenecek>=50 and odenecek<100
    odenecek=odenecek*.8
elif odenecek>=50:
    odenecek=odenecek*.9

print(f"{odenecek}")
    


