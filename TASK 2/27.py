b=int(input("Enter battery percent:"))
d=int(input("Enter drop:"))
for i in range(100):
    b=b-d
    if b<20:
        print("Battery less than 20")
        print(i)
        break
