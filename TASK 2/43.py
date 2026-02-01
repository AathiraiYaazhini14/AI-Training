n=int(input("Enter pass:"))
flag=False
c=0
while n!=0:
    dig=n%10
    if dig==7:
        flag=True
    c+=1
    n//=10
if flag and c>=6:
    print("Strong")
else:
    print("Weak")
