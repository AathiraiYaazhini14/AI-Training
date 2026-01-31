a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==0:
    print("Not quadratic")
d=b**2-(4*a*c)
if d>0:
    print("Real and Distict")
elif d==0:
    print("Real and equal")
else:
    print("Imaginary")
