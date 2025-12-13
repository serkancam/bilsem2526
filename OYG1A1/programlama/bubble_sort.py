dizi=[2,33, 11, 25, 12, 22, 34]
n=7

i=0
sayac=0
while i<n:
    yerdegistirme=False
    j=0
    while j<n-i-1:
        if dizi[j]>dizi[j+1]:
            temp=dizi[j]
            dizi[j]=dizi[j+1]
            dizi[j+1]=temp
            yerdegistirme=True
        j+=1
        sayac+=1
    if not yerdegistirme:
        break
    i+=1

print(dizi,sayac)
    


