# kullanıcı tarafınfan girilen parayı 200,100,50 banknotlar şeklinde veren atm makinesinin kodunu yazınız. Şartımız her seferinde en az adet banknot verilmesidir.
# para olarak sadece 50 ve katları çekilebilir.

istenen_para=int(input("para miktarını giriniz:"))

if(istenen_para%50!=0):
    print("50'nin katı para giriniz:")
    exit()

# çözüm buradan aşağıdaki satırlara yazılacak.
#750
ikiyuz=istenen_para//200#3
yuz=(istenen_para%200)//100
elli=(istenen_para%100)//50
print(f"{ikiyuz} adet 200")
print(f"{yuz} adet 100")
print(f"{elli} adet 50")
