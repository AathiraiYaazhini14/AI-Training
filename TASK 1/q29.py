n=int(input("Enter number:"))
if n==0:
    print("No digts")
s=0
m=n
while m!=0:
    ld=m%10
    s+=ld
    m//=10
print(s)
