# suyun_halleri.py
# suyun üç hali için şartları yazalım(N.Ş.A.)
# gaz -> sicaklik>=100
# sivi -> sicaklik>0 ve sicaklik<100
# kati -> sicaklik<=0 ve sicaklik>=-273.15(mutlak sıfır)

sicaklik=float(input("sıcaklık değerini giriniz:"))

if (sicaklik>=-273.15) and (sicaklik<=0):
    print("katı")
elif (sicaklik>0) and (sicaklik<100):
    print("sıvı")
elif sicaklik>=100:
    print("gaz")
else:
    print("Bu değer olmaz.")
