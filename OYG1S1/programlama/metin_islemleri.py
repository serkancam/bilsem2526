isim="edirne"
soyisim='bilsem'

print(isim+" "+soyisim)
# karakter dizileri string oluyor
# + opertatörü string ifaderi birleştirir(ulamak)

print(20*"isim ")
print("*"*10,"şimdi in operatörü",10*"*")

# * operatörü metni yazılan int kadar tekrarlar

#in operatörü

# in operatörü(içinde birçok eleman olan bir yapının(string,liste,demet...)) verilen karakterin olup olmadığının cevabanını verir(True,False)
# case sensitive(büyük küçük harf duyarlıdır)

print("a" in "Hasan")#True
print("d" in "yalçın")#False
print("a" in "Ali")#False

#string=karakter dizisi "dizi"
print(isim[2])#i 0,1,2...
#[] köşeli parantez, ya bir koleksin biçimindeki bir elemanın adresini(indisini) gösterir ya da bir liste(list) tanımlar

kelime="abrakadabra"
print(kelime[::-1])#arbadakarba tersten yazdırır
print(kelime[::2])#arkdba 
print(kelime[0:3])#abr #ilk 3 karakteri al
print(kelime[-3:])#bra #son 3 karakteri al

