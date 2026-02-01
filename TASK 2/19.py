n=int(input("Enter number:"))
nn=0
while n!=0:
    dig=n%10
    nn=nn*10+dig
    n//=10
for i in range(2,nn):
    if nn%i==0:
        print("Not prime")
        break
else:
    print("Prime")
        
