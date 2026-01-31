n=int(input("Enter number:"))
m=n
s=0
while m!=0:
    dig=m%10
    s+=dig
    m//=10
if n%s==0:
    print("Harshad")
else:
    print("Not Harshad")
