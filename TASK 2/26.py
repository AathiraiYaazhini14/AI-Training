h=int(input("Enter hrs:"))
if h<=2:
    ch=20*h
elif h>2 and h<=5:
    ch=40+(h-2)*15
else:
    ch=40+(3*15)+((h-5)*10)
print(ch)
