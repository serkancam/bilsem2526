"""Değişkenler
1- sayılar
 a- tam sayılar(integer)
 b- ondalıklı(float)
 c- karmaşık sayılar(complex number)
2- karakter dizileri(strings)

pythonda bir değiken tanımlamak demek bir değişken adı ile başlıyan o değişkene = operatörü ile değer(literal) atamak demektir.
Hangi tür/tip değer atanırsa değişken tipi o olur.
python'da değişkenler dinamiktir. Yani her değer atamada o değiken hafızada yeniden oluşur.
"""

a=5
b=8.2
c="bilsem"
print("tipi:",type(a),"adresi:",id(a))
print("tipi:",type(b),"adresi:",id(b))
print("tipi:",type(c),"adresi:",id(c))
a=999_999_999_999
print(a,type(a),id(a))
a = a+1

print(a,type(a),id(a))

t=True
print(type(t))
metin1="bilsem'de bugün"
metin2=' "iyi günler" dedi" '
print(metin1)
print(metin2)
metin3="bilsem:"""#
print(metin3)

#swap işlemi
d1=8
d2=10
d3=12
# d3 d2'nin değerini, d1 d3'nin değerini, d2,d1'ün değerini alsın
#d1-->12,d2-->8,d3-->10
d1,d2,d3=d3,d1,d2

print(f"d1-->{d1},d2-->{d2},d3-->{d3}")
