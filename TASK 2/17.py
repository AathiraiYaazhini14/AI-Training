n=int(input("Enter n:"))
c=0
for i in range(1,n+1):
    num=str(i)
    if '4' not in num:
        c+=1
print(c)
