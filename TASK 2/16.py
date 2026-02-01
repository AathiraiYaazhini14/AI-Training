n=int(input("Enter num:"))
s,p=0,1
while n!=0:
    dig=n%10
    s+=dig
    p*=dig
    n//=10
if s%2==0 and p%3==0:
    print("Valid")
else:
    print("Invalid")
