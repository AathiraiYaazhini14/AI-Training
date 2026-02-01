n=int(input("Enter number:"))
e=0
o=0
while n!=0:
    dig=n%10
    if dig%2==0:
        e+=1
    else:
        o+=1
    n//=10
print(e,o)
