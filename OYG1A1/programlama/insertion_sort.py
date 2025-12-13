dizi=[44,2, 11, 25, 12, 22, 34]
n=7
i=1
while i<n:
    key=dizi[i]
    j=i-1
    while j>=0 and key<dizi[j]:
        dizi[j+1]=dizi[j]
        j-=1
    dizi[j+1]=key
    i+=1
    
print(dizi)
        
        