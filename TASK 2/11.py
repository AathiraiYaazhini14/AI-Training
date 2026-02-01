n=int(input("Enter num:"))
m=n
nn=0
while m!=0:
    dig=m%10
    nn=nn*10+dig
    m//=10
print(nn+n)
