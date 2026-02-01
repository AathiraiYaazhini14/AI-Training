n=int(input("Enter id:"))
if n%7==0:
    c=0
    while n!=0:
        dig=n%10
        c+=1
        n//=0
    if c==6:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
