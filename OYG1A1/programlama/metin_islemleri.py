metin=input("metin giriniz:")

# küçük harfe çevir.
print(metin.lower())
# lower() bir fonksiyon olduğu için parantez açılır kapanır.
# bazı fonsksiyonlar parametre alabilir. 
# split(",")
# print("","","")
# input("promt")
metin_kucuk=metin.lower()
print(metin.split(" "))
print(metin.split("e"))
print("isalpha()","s".isalpha())
print("isalpha()","2".isalpha())
print("isupper()","a".isupper())
print("isupper()","A".isupper())
# karakter dizileri string oluyor
# + opertatörü string ifaderi birleştirir
print("22"+"44")#"2244"
# in operatörü(içinde birçok eleman olan bir yapının(string,liste,demet...))
# case sensitive(büyük küçük harf duyarlıdır)
print("a" in "ali")#True
print("A" in "ali")#False
isim="bilsem"
print(isim[3])#s
#bir değişkenin yanında köşeli parantez vasra ya o bir listedir ya da adres(indis) belirit. 
# yazılımcılar sıfırdan başlar saymaya

###bunlar yalnızca pythonda olur###
print(isim[::-1])#meslib
print(isim[::2])#ble