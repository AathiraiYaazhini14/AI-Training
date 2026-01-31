n=int(input("Enter number:"))
if n==0:
    print("No digts")
c=0
m=n
while m!=0:
    ld=m%10
    c+=1
    m//=10
print(c)
