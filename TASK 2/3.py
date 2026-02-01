n=int(input("Enter number:"))
s=0
if (n%10)%2==0:
    while n!=0:
        dig=n%10
        s+=dig
        n//=10
    if s%3==0:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
