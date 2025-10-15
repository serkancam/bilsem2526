a=345
b=150
k=-1

"""
k=a%b#45

a=b
b=k

k=a%b#15

a=b
b=k

k=a%b#0
print(b)
"""
k=a%b
while k != 0:    
    a=b
    b=k  
    k=a%b

print(b)

 


