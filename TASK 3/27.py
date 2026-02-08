l=list(map(int,input().split()))
k=l.copy()
rl=list(map(int,input().split()))
while True:
    e=l.pop(len(l)-1)
    l.insert(0,e)
    if l==rl:
        print("Yes")
        break
    if k==l:
        print("No")
        break

