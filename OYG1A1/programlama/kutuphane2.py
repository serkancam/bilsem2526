def sesli_say(metin:str):
    say=0
    for krk in metin:
        if krk.isalpha():
            if krk.lower() in "aeiıoöüu":
                say+=1
    return say
def sessiz_say(metin:str):
    say=0
    for krk in metin:
        if krk.isalpha():
            if krk.lower() not in "aeiıoöüu":
                say+=1
    return say

if __name__=="__main__":
    try:
        yol="/home/serkan/Belgeler/bilsem2526/OYG1A1/programlama/isimler.txt"
        baglanti=open(yol,mode="r",encoding="utf-8")
        metin=baglanti.read()
        # print(metin)
        isimler=metin.split(",")
        # print(isimler)
        baglanti.close()
        for isim in isimler:                        
            print(f"{isim} {sesli_say(isim)} sesli {sessiz_say(isim)} sessiz")
    except Exception as e:
        print("hata:",e)