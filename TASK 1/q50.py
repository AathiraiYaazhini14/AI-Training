n=int(input("Enter number:"))
d=int(input("Enter digit:"))
m=n
c=0
while m!=0:
    dig=m%10
    if dig==d:
        c+=1
    m//=10
print(c)
