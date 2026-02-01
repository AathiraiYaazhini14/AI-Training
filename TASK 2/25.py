d=int(input("Enter days:"))
if d>=1 and d<=5:
    fee=2*d
elif d>=6 and d>=10:
    fee=3*d
else:
    fee=5*d
print(fee)
