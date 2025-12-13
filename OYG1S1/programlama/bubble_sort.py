dizi=[8,2,4,3,7,5,6]
n=7#len(dizi)

i=0
adim=0
while i<(n-1):
    degisim=False
    j=0
    while j<(n-i-1):
        adim+=1
        if dizi[j]>dizi[j+1]:
            temp=dizi[j]
            dizi[j]=dizi[j+1]
            dizi[j+1]=temp
            degisim=True
        j+=1
    if not degisim:
        break
    i+=1

print(dizi,adim)
        
    
