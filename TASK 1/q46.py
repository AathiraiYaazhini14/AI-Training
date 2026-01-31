n=int(input("Enter number:"))
s=0
m=n
while m!=0:
    dig=m%10
    fact=1
    for i in range(1,dig+1):
        fact*=i
    s+=fact
    m//=10
if s==n:
    print("Strong")
else:
    print("Not strong")
