n=int(input("Enter num:"))
cou=0
for j in range(2,n+1):
    c=True
    for i in range(2,j):
        if j%i==0:
            c=False
            break
    if c:
        cou+=1
print(cou)
    
