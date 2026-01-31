n=int(input("Enter number:"))
m=n
s=0
while m!=0:
    dig=m%10
    if dig>1:
        for i in range(2,dig):
            if dig%i==0:
                break
        else:
            s+=dig
    m//=10
print(s)
