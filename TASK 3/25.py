l=[]
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
f=True
for i in l:
    if len(set(i))!=len(i):
        f=False
        print("No")
if f:
    print("Yes")
