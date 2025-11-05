# while_dongusu1.py

""" while döngüsü

while şart:
    şart doğru oduğu sürece
    bu bloklar(girinti içindeki herşey çalışır)
    sürekli çalışır    
"""
while '':# 0, 0.0 , "" 
    print("merhaba")
    
# string için "" veya '', int için 0, float için 0.0 dışındaki bütün değerler Bool olarak True sayılır.
print("döngü dışı.")
print(30*"*")
a=1
while a<10:
    print("merhaba:",a)
    a+=1 # a=a+1

print(f"a son değeri:{a}")
print(30*"*")

# bir döngü değişkeni t 5 ten başlasın 13'e kadar(13 dahil) 2 artarak değişsin. ve her t değeri ekrana yazılsın

t=5
while t<=13:
    print(f"t:{t}")
    t=t+2
print(f"t son:{t}")

# bir döngü değişkeni o 15 ten başlasın 3'e kadar(3 dahil ) 2 azalarak değişsin. ve her o değeri ekrana yazılsın

o=15
while o>=3:
    print(f":{o}")
    o=o-2
print(f"t son:{o}")

print(10*"*","uzmanlık sorusu",10*"*")
#################################Bu kod ne yapıyor#################

sayi=2580
k=0
while sayi:
    k=k+sayi%10
    sayi=sayi//10
print(f"sonuç:{k}")



    