n=int(input("Enter number:"))
m=n
lar=-1
slar=-1
while m!=0:
    dig=m%10
    if dig>lar:
        slar=lar
        lar=dig
    m//=10
if lar==slar:
    print(-1)
else:
    print(slar)
