n=int(input("Enter num:"))
s=0
while n!=0:
    dig=n%10
    s+=dig
    n//=10
if s%9==0:
    print("Valid")
else:
    print("Invalid")
