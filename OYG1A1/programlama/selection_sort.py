dizi=[44,2, 11, 25, 12, 22, 34]
n=7
i=0
while i<n:
    enk_indisi=i
    j=i+1
    while j<n:
        if dizi[j]<dizi[enk_indisi]:
            enk_indisi=j
        j+=1
    temp=dizi[i]
    dizi[i]=dizi[enk_indisi]
    dizi[enk_indisi]=temp
    i+=1

print(dizi)
    
        