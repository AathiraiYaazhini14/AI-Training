p=int(input("Enter correct pin:"))
for i in range(3):
    ap=int(input("Enter pin:"))
    if ap==p:
        print("ACCESS GRANTED")
        break
    else:
        print("Incorrect pin try again")
else:
    print("CARD BLOCKED")
