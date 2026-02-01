n=int(input("Enter num:"))
flag=False
if n%10==5:
    while n!=0:
        dig=n%10
        if dig==0:
            flag=True
            break
        n//=10
if flag:
    print("Open")
else:
    print("Locked")
