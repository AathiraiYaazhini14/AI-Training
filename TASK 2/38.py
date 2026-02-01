s=int(input("Enter seats:"))
n=int(input("Enter no of cust:"))
for i in range(n):
    s=s-1
    if s==0:
        print("Housefull")
        break
    else:
        print("Booked")
