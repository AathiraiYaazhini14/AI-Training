n=int(input("Enter n:"))
flag=True
for i in range(n):
    t=int(input("Enter temp:"))
    if t>45:
        flag=False
        print("ALERT")
        break
if flag:
    print("SAFE")
