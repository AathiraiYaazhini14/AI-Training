b=int(input("Enter balance:"))
i=0
if b<10000:
    i=(b*3/100)/12
elif b>=10000 and b<=50000:
    i=(b*5/100)/12
else:
    i=(b*7/100)/12
print(f"{i:.2f}")

