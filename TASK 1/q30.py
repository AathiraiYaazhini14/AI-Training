n=int(input("Enter number:"))
if n==0:
    print("No digts")
p=1
m=n
while m!=0:
    ld=m%10
    p*=ld
    m//=10
print(p)
