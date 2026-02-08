l=list(map(int,input().split()))
k=int(input())
d={}
for i in l:
    d[i]=d.get(i,0)+1
ds=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in range(k):
    print(ds[i][0])
