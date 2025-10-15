# hızı 150 km/sn olan parker sondasi dünyayı ekvator çevresinde nekadar sürede dolaşır. Bu süreyi x dakika y saniye olarak hesaplayınız.
#ekvator r=6379km km pi=3.14
#2*pi*r
pi=3.14
r=6379
hiz=150
cevre=2*pi*r
sure= cevre/hiz
dakika=sure//60
saniye=sure%60

print(f"{dakika}:{saniye}")
