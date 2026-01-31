mrks=float(input("Enter marks:"))
if mrks>=80:
    print("Grade A")
elif mrks<80 and mrks>=70:
    print("Grade B")
elif mrks<70 and mrks>=50:
    print("Grade C")
elif mrks<50 and mrks>=30:
    print("Grade E")
else:
    print("Fail")
