n=list(map(int,input().split()))
for i in range(len(n)-1,0,-1):
    if n[i]==n[i-1]:
        n.pop(i)
print(n)
