n=list(map(int,input().split()))
k=int(input())
for i in range(k):
    s=n.pop()
    n.insert(0,s)
print(n)
