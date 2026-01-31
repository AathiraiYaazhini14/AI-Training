year=int(input("Enter year:"))
if year%4==0:
    if year%100!=0:
        print("Yes its a leap year")
    else:
        print("Not a leap year")
elif year%400==0:
    print("Yes its a leap year")
else:
        print("Not a leap year")
        
