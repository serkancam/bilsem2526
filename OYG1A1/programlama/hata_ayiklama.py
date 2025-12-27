try:
    yas=int(input("yaşınızı giriniz:"))
    sonuc=100/(98-yas)
except ZeroDivisionError as zde:
    print("sıfıra bölme hatası.",zde)
except BaseException as be:
    print("hata: Sayı çevirme hatası.",be)

except Exception as e:
    print("hata var.",e)
else:
    print(f"yaşınız:{yas}")
finally:
    print("her türlü çalışırım.")
