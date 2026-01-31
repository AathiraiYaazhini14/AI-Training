shape=input("Rectangle or circle (r/c):")
if shape=="r" or shape=="R":
    l=float(input("Enter length:"))
    b=float(input("Enter breadth:"))
    print("Area of rectangle =",l*b)
    print("Perimeter of rectange =",2*(l+b))
elif shape=="c" or shape=="C":
    r=float(input("Enter radius:"))
    print("Circumference of circle:",2*3.14*r)
else:
    print("Invalid input")
