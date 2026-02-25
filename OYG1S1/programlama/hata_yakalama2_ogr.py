#isimler.txt dosyasındaki isimleri bir listeye aktarınız
# bu isimlerde geçen sesli ve sessiz harf sayılarını ekrana her isim için tek tek yazdırınız.

#örnek çıktı
# çağrı 2 sesli 3 sessiz
# selim 2 sesli 3 sessiz
# dosya ve kaynaktan veri okuma/yazma işlemleri her zaman try bloğu içinde olmlalıdır.
def sesli_say(metin:str):
    say=0
    for h in metin:
        if h.isalpha() and h in "aeıioöuü":
            say+=1
    return say

def sessiz_say(metin:str):
    say=0
    for h in metin:
        if h.isalpha() and h not in "aeıioöuü":
            say+=1
    return say      
if __name__=="__main__":
    try:
        yol="/home/serkan/Belgeler/bilsem2526/OYG1S1/programlama/isimler.txt"
        dosya=open(yol,mode="r",encoding="utf-8")
        metin=dosya.read()
        dosya.close()
        metinler=metin.split(",")
        for k in metinler:    
                
            print(f"{k} {sesli_say(k)} sesli {sessiz_say(k)} sessiz")
    except Exception as e:
        pass
        