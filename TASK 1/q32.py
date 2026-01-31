n=int(input("Enter number:"))
m=n
rev=0
while m!=0:
    ld=m%10
    rev=rev*10+ld
    m//=10
print(rev)
