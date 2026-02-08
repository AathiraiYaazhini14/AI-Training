l=list(map(int,input().split()))
s=set(l)
if list(s)!=l:
    print("Duplicates!!!")
else:
    print("Safe")
