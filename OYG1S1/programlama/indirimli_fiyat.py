# Bir kafede satılan ürünlerin fiyatları şöyledir: Çay (5 TL), Kahve (10 TL), Tatlı (15 TL). Kullanıcıdan kaç adet çay, kahve ve tatlı aldığını sorun. Toplam tutarı hesaplayın ve aşağıdaki indirim kurallarını uygulayarak son ödemesi gereken tutarı ekrana yazdırın:
#     Toplam tutar 50 TL veya daha fazlaysa, %10 indirim yapın.
#     Toplam tutar 100 TL veya daha fazlaysa, %20 indirim yapın.
#     Diğer durumlarda indirim uygulamayın.


cay_fiyati=5
kahve_fiyati=10
tatli_fiyati=15

cay_adedi=int(input("cay adedi:"))
kahve_adedi=int(input("kahve adedi:"))
tatli_adedi=int(input("tatli adadi:"))

fiyat=(cay_adedi*cay_fiyati)+(kahve_adedi*kahve_fiyati)+(tatli_adedi*tatli_fiyati)


if fiyat>=50 and fiyat<100:
    fiyat=fiyat*0.9
elif fiyat>=100:
    fiyat=fiyat*0.8

print(f"ödenecek tutar:{fiyat}")
    
    