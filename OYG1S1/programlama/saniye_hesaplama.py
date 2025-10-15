#kullanıcıdan saniye değerini alarak, aldığı bilgiyi saat:dakika:saniye şeklinde yazan programı python ile kodlayınız.
#örnekler
#giriş:155
#0:2:35
#giriş:7305
#2:1:45
girilen_saniye=int(input("saniye değeri giriniz:"))

saat=girilen_saniye//3600
dakika=(girilen_saniye%3600)//60
saniye=girilen_saniye%60#(girilen_saniye-3600*saat-dakika*60)

print(f"{saat}:{dakika}:{saniye}")


