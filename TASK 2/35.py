n=int(input("Enter pin:"))
s,c=0,0
while n!=0:
    dig=n%10
    c+=1
    s+=dig
    n//=10
if s>15 and c==4:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
