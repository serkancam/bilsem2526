dizi=[8,2,4,3,7,5,6]
n=7#len(dizi)

i=0
while i<n:
    enkucuk_indisi=i
    j=i+1
    while j<n:
        if dizi[j]<dizi[enkucuk_indisi]:
            enkucuk_indisi=j
        j+=1
    temp=dizi[i]
    dizi[i]=dizi[enkucuk_indisi]
    dizi[enkucuk_indisi]=temp
    i+=1
print(dizi)