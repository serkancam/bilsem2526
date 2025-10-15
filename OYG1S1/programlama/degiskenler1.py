"""
Bir yazılım dili için öğrenilmesi gereken temeller
1- Veri türleri(değişkenler)
2- operatörler(+,-,**,%,and,or.....)
3- karar-kontrol yapıları (if,if-elif-else,while,for...)
4- fonksiyonlar(dahili,harici, kullaıcı tanımlı)
5- koleksiyonlar
6- modüller/kütüphaneler
7- nesne/sınıf kavramı ve kullanımı (OOP-nesne yönelimli programlama)    
8- hata ayıklama   
    
"""
print("merhaba.")
"""değişken ve dosya isimlendirme kuralları
1- dosya ve değişken isimlerinde sadece ingiliz alfabesi harfleri, rakamlar ve alt çizgi _ karakterleri olabilir.
2- dosya ve değişken isimleri rakam ile başlayamaz.
"""

#python dili tipleri dinamiktir.
a=5
b=8
print(type(a),id(a))
print(type(b),id(b))
a="ali"
b=True
print(type(a),id(a))
print(type(b),id(b))
print(20*"*")
sayi=10
print(id(sayi))
sayi=sayi+10
print(id(sayi))