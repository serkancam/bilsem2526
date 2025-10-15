""" while döngüsü

while şart:
    şart doğru oduğu sürece
    bu bloklar(girinti içindeki herşey çalışır)
    sürekli çalışır    
"""
i=10
while i>2:
    print(f"{i} merhaba")
    i=i-1
print("i son",i)

print(30*"*")

#döngü değişkeni t olsun ve 1 den başlasın. 13'e kadar ekrana sayıalrı yazdıran kodu yazın.
t=1
while t<14:#t<=13
    
    print(f"{t}")
    t=t+1
    
    
print("############bu kod ne yapıyor#################")
sayi=int(input("sayi giriniz:"))
x=0
while sayi:
    x=x+sayi%10
    sayi=sayi//10
    
print(x)

