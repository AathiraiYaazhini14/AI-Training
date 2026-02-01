d=int(input("Enter dis:"))
if d<=5:
    ch=d*10
elif d>=6 and d<=15:
    ch=5*10+((d-5)*8)
else:
    ch=50+10*8+((d-15)*6)
print(ch)
