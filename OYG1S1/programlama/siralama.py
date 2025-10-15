listem=[10,-1,8,3,7,2]

eleman_sayisi=len(listem)

# i=0
# enks=listem[0]
# while i<eleman_sayisi:#i küçük iken 6 dan
#     print(listem[i])
#     if listem[i]<enks:
#         enks=listem[i]
#     i=i+1

# print(f"en küçük sayı:{enks}")

i=0
while i<eleman_sayisi:
    k=i+1
    while k<eleman_sayisi:
        if listem[k]<listem[i]:
            temp=listem[k]
            listem[k]=listem[i]
            listem[i]=temp
        k=k+1
    i=i+1

print(listem)
