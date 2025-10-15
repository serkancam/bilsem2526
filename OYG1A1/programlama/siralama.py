listem=[2,5,-9,0,55,1,-4]

i=0
k=0
eleman_sayisi=len(listem)
while i<eleman_sayisi:
    k=i+1
    while k<eleman_sayisi:        
        #print(f"i={i}-k={k}")
        if listem[k]<listem[i]:
            # temp=listem[i]
            # listem[i]=listem[k]
            # listem[k]=temp
            listem[k],listem[i]=listem[i],listem[k]
            
        k=k+1
    i=i+1

print(listem)