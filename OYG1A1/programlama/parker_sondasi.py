# hızı 150 km/sn olan parker sondasi dünyayı ekvator çevresinde nekadar sürede dolaşır. Bu süreyi x dakika y saniye olarak hesaplayınız.
#ekvator r=6379km km pi=3.14
#2*pi*r

PI=3.14 #sabit tanımladım
r=6379
cevre=2*PI*r
gecen_saniye=cevre/150 #xxx.yyyy

dakika=gecen_saniye//60 
saniye=gecen_saniye%60#gecen_saniye-dakika*60

print(f"{dakika}:{saniye}")

# sayılarla işlem yaparken işlemler sonucu oluşan sayının tam sayı mı? ondalıklı sayı mı? olcağını bilmek önemlidir.
# bunun için:
#1- işleme giren sayılardan biri dahi ondalıklı ise sonuç ondalıklı çıkar
#2- işlem bölme(/) ise sonuç mutlaka ondalıklı çıkar
#3- diğer şartlarda sonuç hep tam sayıdır.







