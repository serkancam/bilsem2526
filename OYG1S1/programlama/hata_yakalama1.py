# kullanıcdan aldığı boy ve kilo değeri ile bki hesaplasın

try:
    isim=input("isim:")
    boy=float(input("boy:"))
    kilo=float(input("kilo:"))
    bki=kilo/(boy**2)
except ZeroDivisionError as zde:
    print(f"sıfıra bölme hatası:{zde}")
except ValueError as ve:
    print(f"dönüşüm hatası:{ve}")
except Exception as e:
    print(f"hata:{e}")

else:
    print(f"bki:{bki}")
finally:
    print("try bloğu bitiş.")

print("program btti.")