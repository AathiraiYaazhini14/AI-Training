n=int(input("Enter num:"))
e,o=0,0
for i in range(n+1):
    if i%2==0:
        e+=1
    else:
        o+=1
print("Even:",e)
print("Odd:",o)
