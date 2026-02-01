n=int(input("Enter n:"))
d=int(input("Enter d:"))
c=0
while n!=0:
    dig=n%10
    if dig==d:
        c+=1
    n//=10
print(c)
