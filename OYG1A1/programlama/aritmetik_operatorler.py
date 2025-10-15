"+,-,*,/,%,//,**,"

s1="3"
s2="5"
# operaötlerin bir kısmı iki operand alır, bir kısmı bir operand alır.
print(s1+s2)
girilen_saniye=int(input("saniye giriniz:"))#-0...9

#veri olarak girilen saniye değerini saat:dakika:saniye şeklinde yazan kodu yazınız.
#155
#0:2:35
#1300
saat=girilen_saniye//3600
kalan=girilen_saniye%3600
dakika=kalan//60
saniye=kalan%60

print(f"{saat}:{dakika}:{saniye}")
print(saat,":",dakika,":",saniye,sep="")
