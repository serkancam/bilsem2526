dizi=[8,2,4,3,7,5,6]
n=7#len(dizi)


i=1
while i<n:
    deger=dizi[i]
    j=i-1
    while j>=0 and deger<dizi[j]:
        dizi[j+1]=dizi[j]#soldakini sağa aktar
        j-=1
    dizi[j+1]=deger
    i+=1
print(dizi)
    