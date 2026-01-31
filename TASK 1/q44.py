a=int(input("Enter number:"))
b=int(input("Enter number:"))
hcf=1
for i in range(2,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)
