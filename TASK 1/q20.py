cp=float(input("Enter cost price:"))
sp=float(input("Enter selling price:"))
if cp>sp:
    print("Loss")
elif cp<sp:
    print("Profit")
else:
    print("No profit no loss")
