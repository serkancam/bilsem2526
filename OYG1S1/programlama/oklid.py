a=345
b=150
"""
k=a%b#45
a=b
b=k
#2.
k=a%b#15
a=b
b=k
#3.
k=a%b#0
a=b
b=k

print(f"ebob(345,150)={a} ")
"""
a=int(input("büyük sayı:"))
b=int(input("küçük sayı:"))
k=-1
a1=a
b1=b
while k != 0:#k değeri sıfırdan farklı iken aşağıdaki komutları yap
    k=a%b
    a=b
    b=k

print(f"ebob({a1},{b1})={a}")

     
