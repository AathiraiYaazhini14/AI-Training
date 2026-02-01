n=int(input("Enter number:"))
s=0
while n!=0:
    dig=n%10
    if dig>1:
        for i in range(2,dig):
            if dig%i==0:
                break
        else:
            s+=dig
            print(dig)
    n//=10
print(s)
