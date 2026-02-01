l=float(input("Enter lit:"))
p=float(input("Enter price:"))
bill=int(l*p)
ld=bill%10
if ld>=0 and ld<=4:
    bill=bill-ld
else:
    bill=bill+(10-ld)
print(bill)
