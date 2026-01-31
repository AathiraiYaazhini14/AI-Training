n=int(input("Enter num:"))
c=True
for i in range(2,n):
    if n%i==0:
        c=False
        print("Not prime")
        break
if c:
    print("Prime")
    
