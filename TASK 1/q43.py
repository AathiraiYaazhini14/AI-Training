a=int(input("Enter  number:"))
b=int(input("Enter  number:"))
l=max(a,b)
while True:
    if l%a==0 and l%b==0:
        print("LCM:",l)
        break
    l+=1
