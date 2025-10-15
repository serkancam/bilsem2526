#suyun üç hali için şartları yazalım(N.Ş.A.)
# gaz -> sicaklik>=100
# sivi -> sicaklik>0 ve sicaklik<100
# kati -> sicaklik<=0 ve sicaklik>=-273.2

sicaklik=float(input("sıcaklık değeri:"))

if sicaklik>=100:
    print("gaz")
    print("Haktan haklı.")
elif sicaklik>0 and sicaklik<100:
    print("sıvı")
    print("ihtiyaçlar teneffüste")
elif sicaklik<=0 and sicaklik>=-273.15:
    print("katı")
    print("bu sefer kesin")
else:
    print("böyle bir sıcaklık değeri yok.")
    print("herkes haklı")

        
    


