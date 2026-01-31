n=int(input("Enter number:"))
m=n
arm=0
while m!=0:
    ld=m%10
    arm+=ld**3
    m//=10
if arm==n:
    print("Armstrong")
else:
    print("Not armstrong")
